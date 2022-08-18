# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Users\WAEL\Documents\pyproject\chromedriver.exe" #path of driver

driver=webdriver.Chrome(PATH) #to open the google chrome driver
driver.get("https://nerd.black-ch.com/stu/login.php") # the url that the app will work on it

print(driver.title) # get the title
driver.find_element(By.ID,'user').send_keys("1@1") # search on element have ID user and put on it 1@1
driver.find_element(By.NAME,'password').send_keys("1") # search on element have name password and put on it 1
driver.find_element(By.NAME,'login').click() #find elemant have name login and click on it
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
