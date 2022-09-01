from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing import Process
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import os
import socket

def ipcheck():
    return socket.gethostbyname(socket.getfqdn())

def get_LoadTimes(url):
    dsproxys = ["1#","2#","3#","4#"]

    f = open("report_proxy_test.txt",'a')
    
    for dsproxy in dsproxys:
        chromePath = "D:/Python/speedcheck/chromedriver"
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("disable-gpu")

        with webdriver.Chrome(chromePath, chrome_options=options) as driver:
            driver.get(url)

            ''' Use Navigation Timing  API to calculate the timings that matter the most '''   
            navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            responseStart = driver.execute_script("return window.performance.timing.responseStart")

            ''' Calculate the performance'''
            backendPerformance_calc = responseStart - navigationStart
            loadTime = round(float(backendPerformance_calc)/1000,2)
            data = ipcheck()," -> ",dsproxy," -> ","url   :   ",loadTime,"sec"
            print(data)
            f.write(data + "\n")
            f.close()
    

def get_LoadTimes_cron():
    get_LoadTimes("https://www.naver.com")
    get_LoadTimes("https://www.daum.net")
    get_LoadTimes("https://www.google.com")

sched = BlockingScheduler()
sched.add_job(get_LoadTimes_cron, 'cron', minute='*/5')
print("Starting scripts...")
sched.start()

"""
if __name__ == "__main__":
    start_time = time.time()
    procs = []
    urls = ["https://www.naver.com", 
            "https://www.daum.net", 
            "https://www.google.com"]
    

    for url in urls:
        for dsproxy in dsproxys:
            process = Process(target=get_LoadTimes, args=(url, dsproxy))
            process.start()
            procs.append(process)
        # proxy1 = Process(target=get_LoadTimes, args=(url, proxys[0]))       
        # proxy2 = Process(target=get_LoadTimes, args=(url, proxys[1]))
        # proxy3 = Process(target=get_LoadTimes, args=(url, proxys[2]))
        # proxy4 = Process(target=get_LoadTimes, args=(url, proxys[3]))
        # procs.append(proxy1)
        # procs.append(proxy2)
        # procs.append(proxy3)
        # procs.append(proxy4)
        # for proc in procs:  # 프로세스 시작
        #     proc.start()
        for proc in procs:  # 프로세스 종료 대기
            proc.join()
        procs = []  # 프로세스 초기화

    print("--- %s seconds --" % (time.time() - start_time))
"""