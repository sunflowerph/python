#coding=utf-8
from selenium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'f6e06a1c'
desired_caps['appPackage'] = 'com.tencent.news'
desired_caps['appActivity'] = 'com.tencent.news.activity.SplashActivity'

driver = webdriver.Remote('http://0000:4723/wd/hub', desired_caps)

#name='com.tencent.news.activity.SplashActivity'
