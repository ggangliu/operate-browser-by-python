# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 23:40:35 2018

@author: 刚刚刘
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

option  = webdriver.FirefoxOptions()
option.add_argument('disable-infobars')
#option.add_argument('headless')

browser = webdriver.Firefox(options=option)
browser.get('https://www.google.com')
browser.execute_script('window.open()')
browser.get('https://www.taobao.com')

input = browser.find_element_by_id('lst-ib')
input.send_keys('who am i')
#input.send_keys(Keys.ENTER)

button = browser.find_element_by_name('btnK')
button.click()


#browser.close()