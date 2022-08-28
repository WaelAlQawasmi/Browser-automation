import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# mtime=time.localtime()
# yu = time.strftime("%H:%M:%S", mtime)
# while yu !="11:40:25":
#      mtime = time.localtime()
#      yu = time.strftime("%H:%M:%S", mtime)
#      print(yu)

PATH = r"C:\Users\HOME\Documents\chromrDriver\chromedriver_win32\chromedriver.exe" #path of driver

driver=webdriver.Chrome(PATH) #to open the google chrome driver
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# to open the Google Chrome driver
driver.get("https://visitjordan.gov.jo/travelcars/")  # the url that the app will work on it


driver.find_element(By.XPATH, "//div[@class='radiorow'][2]").click()
driver.find_element(By.NAME, 'txtName').send_keys("داهود على محمد قطيش") # عدل الاسم
driver.find_element(By.NAME, 'txtPassportNu').send_keys("P976344") # رقم الجواز
driver.find_element(By.NAME, 'txtIDNumber').send_keys("9691014308") #الرقم الوطني
driver.find_element(By.NAME, 'txtCarNumber').send_keys("50-39114") # رقم السيارة
driver.find_element(By.NAME, 'txtEmail').send_keys("walzoubi32@yahoo.com") # الب# ريد
driver.find_element(By.NAME, 'txtMobile').send_keys("786043200") # البريد

driver.find_element(By.XPATH, "//select[@name='ddlNationality']/option[text()='الأردن']").click() #الجنسية
driver.find_element(By.XPATH, "//select[@name='ddlCountryCode']/option[text()='الأردن - 00962']").click() #رمز الدولة
driver.find_element(By.XPATH, "//div[@class='nkcheckbox'][1]").click()


mtime=time.localtime()
yu = time.strftime("%H:%M:%S", mtime)
print(yu)
while yu != "03:29:25" :
    mtime = time.localtime()
    yu = time.strftime("%H:%M:%S", mtime)

driver.find_element(By.ID,'SubmitInvest').click()






