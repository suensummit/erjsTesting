from selenium import webdriver
import csv

# set test sample ec site
#url = "https://"
url = "https://duckduckgo.com/"

#for x in testbot:
#	for action in testbot(x).act_list:
driver1 = webdriver.PhantomJS()
driver1.get(url)
driver2 = webdriver.PhantomJS()
driver2.get(url)
driver3 = webdriver.PhantomJS()
driver3.get(url)
#driver.get(url)
#driver.find_element_by_id().send_keys()
#driver.find_element_by_id().click()
driver1.quit()
driver2.quit()
driver3.quit()
