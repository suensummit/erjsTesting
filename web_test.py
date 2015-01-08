from selenium import webdriver
from pandas as pd
import csv
import time

# load test data
with open('web_test_funnel.csv', 'rb') as f:
    reader = csv.reader(f)
    testbot_raw = list(reader)

testbot = sorted(testbot_raw, key=lambda testbot_raw: testbot_raw[2])

# set test sample ec url
url = "file:///Users/summitsuen/Documents/erjsTesting/index.html"
#url = "https://suensummit.github.io/erjsTesting/"

# 
driver = {}
k = 0
while k <= len(ssid):
    key = ssid[k]
    value = webdriver.PhantomJS()
    driver[key] = value
    k += 1

#for x in range(len(ssid)):
for x in ssid:
	for action in testbot(x).act_list:
		driver[x].get(url)
		driver[x].find_element_by_id().click()
		driver[x].quit()

#driver.find_element_by_id().send_keys()
#driver.find_element_by_id().click()
