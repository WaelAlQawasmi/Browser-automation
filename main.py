# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Users\HOME\Documents\chromrDriver\chromedriver_win32\chromedriver.exe" #path of driver

driver = webdriver.Chrome(PATH)
# to open the Google Chrome driver
driver.get("https://visitjordan.gov.jo/travelcars/")  # the url that the app will work on it


driver.find_element(By.XPATH, "//div[@class='radiorow'][2]").click()
driver.find_element(By.NAME, 'txtName').send_keys("داهود على محمد قطيش") # عدل الاسم
driver.find_element(By.NAME, 'txtPassportNu').send_keys("P976344") # عدل الاسم


driver.find_element(By.NAME, 'txtName').send_keys("داهود على محمد قطيش") # عدل الاسم
driver.find_element(By.NAME, 'txtPassportNu').send_keys("P976344") # رقم الجواز
driver.find_element(By.NAME, 'txtIDNumber').send_keys("9691014308") #الرقم الوطني
driver.find_element(By.NAME, 'txtCarNumber').send_keys("50-39114") # رقم السيارة
driver.find_element(By.NAME, 'txtEmail').send_keys("walzoubi32@yahoo.com") # البريد
