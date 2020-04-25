# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:42:05 2020

@author: bijuangalees
"""

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser=webdriver.Firefox(executable_path="D:\geckodriver.exe")
browser.get("https://web.whatsapp.com/")

elem=browser.find_element_by_link_text('FRIENDS')
elem.click()
search=browser.find_element_by_id('q')
search.send_keys('Download')
wait=WebDriveWait(driver,600)