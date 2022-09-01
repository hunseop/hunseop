from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Pool
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import socket
import csv

''' 기본 정보 '''
# URL 정보 파일 불러오기
urlList = open('D:\\02_Programming\\Python\\old\\speedcheck\\urlList.txt', 'r').read().split('\n')

# 프록시 정보
proxyList = ['Proxy#1', 'Proxy#2', 'Proxy#3', 'Proxy#4']

# chromedriver 경로지정
chromePath = "D:\\02_Programming\\Python\\old\\speedcheck\\chromedriver.exe"

# 시간 변수
currentDate = str(datetime.now().strftime("%y/%m/%d")).replace("/","")

# 시간 체크 함수
def timeCheck():
    return datetime.now().strftime("%H:%M:%S")

# IP 체크 함수
def ipCheck():
    return socket.gethostbyname(socket.getfqdn())

# 시간 측정 함수
def getLoadTimes(url_proxy):
    proxy, url = url_proxy

    """
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy":proxy,
        "ftpProxy":proxy,
        "sslProxy":proxy,
        "proxyType":"MANUAL"
    }
    """
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    options.add_argument("no-sandbox")
    options.add_argument("disable-software-rasterizer")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    # driver = webdriver.Chrome(chromePath, chrome_options=options)
    
    driver.get(url)

    ''' Use Navigation Timing  API to calculate the timings that matter the most '''   
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")

    ''' Calculate the performance'''
    backendPerformance_calc = responseStart - navigationStart
    loadingTime = round(float(backendPerformance_calc)/1000, 2)

    driver.quit()

    return proxy, url, loadingTime

# 메인 함수
def startScript():
    url_proxy = []

    for url in urlList:
        for proxy in proxyList:
            url_proxy.append((proxy, url))

    results = Pool(4).map(getLoadTimes, url_proxy)

    with open(currentDate+"_test_time.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        for result in results:
            res=list(result)
            res.insert(0,timeCheck())
            print(res)
            writer.writerow(res)

if __name__=='__main__':
    startScript()
    # # 스케줄링
    # sched = BlockingScheduler()
    # sched.add_job(startScript, 'cron', minute='*/2')
    # print("Starting script...")
    # sched.start()