from selenium import webdriver
import csv
import time

# load test data

# set test sample ec url
url = "https://suensummit.github.io/erjsTesting/"

# 
driver = {}
k = 0
while k <= len(ssid):
    key = k
    value = webdriver.PhantomJS()
    driver[key] = value
    k += 1

for x in range(len(ssid)):
	for action in testbot(x).act_list:
		driver[x].get(url)
		time.sleep(1)
		driver[x].find_element_by_id().click()
		time.sleep(1)
		driver[x].quit()

#driver.find_element_by_id().send_keys()
#driver.find_element_by_id().click()
