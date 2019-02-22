#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import requests
import json
from selenium import webdriver
def sendto_dingtalk(**x):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a9ac2379c2eb09ef75d4108ccc8ee119ce59d3d364f350d68d679ccc2cb8cdf7'
    HEADERS = {
        "Content-Type": "application/json; charset=utf-8"
    }
    d = {
        "msgtype": "text",
        "text":{
            "content": x
        },
        "at":{
            "atMobiles":[
                "17600147211",
                "13691281371"
            ],
            "isAtAll":"false"
        }
    }
    d=json.dumps(d)
    requests.post(url, data=d, headers=HEADERS)
def check():
    source = ["http://www.google.com","https://www.baidu.com/"]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="/usr/local/bin/chromedriver")
    # driver = webdriver.Chrome("/Users/edz/Downloads/chromedriver")
    while True:
        target = []
        for i in source:
            driver.get(i)
            navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
            blanktime = responseStart - navigationStart
            if blanktime > 500:
                target.append(i)
        if len(target) > 0:
            msg = {"白屏时间过长的URL:":target}
            sendto_dingtalk(**msg)
if __name__ == "__main__":
    check()