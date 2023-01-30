
#How to change your password in Instagram by Python Automation using PYCHARM.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.maximize_window() #maximize the window
driver.get("https://www.instagram.com/accounts/login/") #Instagram login page link
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(2)
driver.find_element(By.XPATH, "//form/label/input").send_keys("rathishravi23@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//div/button").click()
time.sleep(3)
driver.get("https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHfVnreYSjBBXwy87Jpu0se5MfarEoZk-YYsjVGrFy1CUivZAIo5bG_YE0N8cs8HEG4e1kQPIw&flowName=GlifWebSignIn&flowEntry=ServiceLogin") # email login link
time.sleep(2)
driver.find_element(By.XPATH, "//div/input[1]").send_keys("rathishravi23@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH, "//div/button"). click()
time.sleep(3)
driver.find_element(By.XPATH, "//div/input[1]").send_keys("rathishravi23022000@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH, "//div/button[1]"). click()
time.sleep(40)
#driver.find_element(By.XPATH, "").send_keys("")
#time.sleep(1)
#driver.find_element(By.XPATH, "")