''' Import the necessary packages required for execution '''
from selenium import webdriver
from multiprocessing import Pool # Pool import하기
import time

''' Chrome web driver interface'''
urls = ["http://www.naver.com", 
        "http://www.daum.net", 
        "http://www.youtube.com", 
        "http://www.google.com"]
proxys = ["1#","2#","3#","4#"]

chromePath = "D:/Python/speedcheck/chromedriver"

def get_LoadTimes(url: str,proxy):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(chromePath, chrome_options=options)
    driver.get(url)

    ''' Use Navigation Timing  API to calculate the timings that matter the most '''   
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    #domComplete = driver.execute_script("return window.performance.timing.domComplete")

    ''' Calculate the performance'''
    backendPerformance_calc = responseStart - navigationStart
    #frontendPerformance_calc = domComplete - responseStart
    # print("proxy {0}".format(proxy))
    # print("link : ",url)
    # print("Back End: %s" % backendPerformance_calc)
    #print("Front End: %s" % frontendPerformance_calc)

    #driver.implicitly_wait(3)
    #driver.get_screenshot_as_file('naver_main_headless.png') # 검증용 스크린샷
    
    driver.quit()


def func(a, b):
    print(a)
    print(b)
    return a + b


if __name__=='__main__':
    start_time = time.time()

    # with Pool(processes=4) as pool:  
    #     pool.map(partial(test, url=urls), proxys)
    a=[1,2,3]
    b=[5,6,7]
    arg=[]
    for i 
    pool = Pool(3)
    pool.map(func, arg)

    print("--- %s seconds ---" % (time.time() - start_time))