from selenium import webdriver
import csv
import time

# set test sample ec site
#url = "https://"
url = "https://duckduckgo.com/"

#for x in testbot:
#	for action in testbot(x).act_list:
driver = webdriver.PhantomJS()
driver.get(url)
time.sleep(3)
driver.set_window_size(1120, 550)
driver2 = webdriver.Firefox()
driver2.get(url)
time.sleep(3)
driver3 = webdriver.Firefox()
driver3.get(url)
time.sleep(3)
driver3.set_window_size(1120, 550)
#driver.get(url)
#driver.find_element_by_id().send_keys()
#driver.find_element_by_id().click()
driver.quit()
time.sleep(3)
driver2.quit()
time.sleep(3)
driver3.quit()
