''' Import the necessary packages required for execution '''
from selenium import webdriver
from multiprocessing import Pool
import time

chromePath = "D:/Python/speedcheck/chromedriver"

def get_LoadTimes(arg):

    url=arg.split("_")[0]
    proxy=arg.split("_")[1]

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(chromePath, chrome_options=options)
    driver.get(url)

    ''' Use Navigation Timing  API to calculate the timings that matter the most '''   
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")

    ''' Calculate the performance'''
    backendPerformance_calc = responseStart - navigationStart
    loadTime = round(float(backendPerformance_calc)/1000, 2)
    driver.quit()

    return proxy, url, loadTime


if __name__=='__main__':
    start_time = time.time()

    proxys = ["1#","2#","3#","4#"]
    urls = ["http://www.naver.com", 
            "http://www.daum.net",  
            "http://www.google.com"]

    arg=[]
    for proxy in proxys:
        for url in urls:
            url_proxy = url+"_"+proxy
            arg.append(url_proxy)

    with Pool(processes=4) as pool:  
        print(pool.map(get_LoadTimes, arg))

    print("--- %s seconds ---" % (time.time() - start_time))