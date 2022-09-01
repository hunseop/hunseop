from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import socket
"""
import os
from elasticsearch import Elasticsearch

def srvHealthCheck(es):
    health = es.cluster.health()
    return health
"""

def ipcheck():
    return socket.gethostbyname(socket.getfqdn())

def check_web_with_proxy(hlink):
    dsproxys = {"12.26.201.11:8080","12.26.201.12:8080","12.26.201.13:8080","12.26.201.14:8080"}

    f = open("report_proxy_test.txt",'a')

    for dsproxy in dsproxys:

        """
        webdriver.DesiredCapabilities.CHROME['proxy']={
            "httpProxy":dsproxy,
            "ftpProxy":dsproxy,
            "sslProxy":dsproxy.
            "proxyType":"MANUAL",
        }
        """
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        with webdriver.Chrome(options=chrome_options) as driver:
            wait = WebDriverWait(driver, 10)
            driver.get(hlink)
            navigationStart=driver.execute_script("return window.performance.timing.navigationStart")
            responseStart=driver.execute_script("return window.performance.timing.respoenseStart")
            domComplete=driver.execute_script("return window.performance.timing.domComplete")
            
            backendPerformance_calc = responseStart - navigationStart
            now = datetime.now()
            current_time = now.strftime("%y/%m/%d %H:%M:%S")
            backend = "%s" % backendPerformance_calc
            
            backend = round((int(backend)/1000),2)
            data = ipcheck() + "->"+dsproxy+"->"+hlink+"    :   "+current_time+","+backend;
            print(data)
            f.write(data + "\n")
            f.colse()

def check_web_with_proxy_cron():
    check_web_with_proxy("https://www.google.com")
    check_web_with_proxy("https://www.naver.com")
    check_web_with_proxy("https://www.daum.net")
    check_web_with_proxy("https://www.youtube.com")

#check_web_with_proxy_cron()

sched = BlockingScheduler()
sched.add_job(check_web_with_proxy_cron, 'cron', minute='*/5')
print("Starting script...")
sched.start()