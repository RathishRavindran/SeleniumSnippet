import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window() #maximize the window
driver.get("https://www.youtube.com/") #YouTube link
time.sleep(5)
driver.find_element(By.NAME, "search_query").send_keys("Vaadi vaadi") #Song name which you need to mention
driver.find_element(By.ID, "search-icon-legacy").click() #By clicking on search it will direct you to the song name you mentioned
time.sleep(5)
driver.find_element(By.CLASS_NAME, "style-scope ytd-video-renderer").click() #As you mentioned the song name this will click the first song which is coming infront row
time.sleep(1000000)