# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:49:04 2020

@author: bijuangalees
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox(executable_path="D:\geckodriver.exe")
driver.get("https://web.watsapp.com/")
wait=WebDriveWait(driver,600)
target='"sreenath"'
string="Message sent using python I love u charakke"
x_arg='//span[contains(@title, '+ target +')]'
target=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box=driver.find_elemet_by_class_name('_1Plpp')
for i in range(50):
    input_box.send_keys(string+Keys.Enter)


