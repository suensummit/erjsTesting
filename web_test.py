from selenium import webdriver
from pandas import *
import csv
import time

# load test data
with open('web_test_funnel.csv', 'rb') as f:
	reader = csv.reader(f)
	testbot_raw = list(reader)

testbot = sorted(testbot_raw, key=lambda testbot_raw: testbot_raw[2])
df = DataFrame(testbot, columns = testbot[len(testbot)-1])

# set test sample ec url
url = "file:///Users/summitsuen/Documents/erjsTesting/index.html"
#url = "https://suensummit.github.io/erjsTesting/"

# 
driver = {}
k = 0
ssid = df.ssid.unique()
while k < len(ssid)-1:
	key = ssid[k]
	value = webdriver.PhantomJS()
	#value = webdriver.Firefox()
	driver[key] = value
	k += 1

# send actions from testbot
for k in range(len(df)-2):
	driver[df.ssid[k]].get(url)
	driver[df.ssid[k]].find_element_by_id('uid').send_keys(df.uid[k])
	driver[df.ssid[k]].find_element_by_id('act').send_keys(df.act[k])
	driver[df.ssid[k]].find_element_by_id('cat').send_keys(df.cat[k])
	driver[df.ssid[k]].find_element_by_id('pid').send_keys(df.pid[k])
	driver[df.ssid[k]].find_element_by_id('eruid').send_keys(df.eruid[k])
	print 'It is the ' + str(k+1) + 'th testbot\n'
	#driver[df.ssid[k].find_element_by_id().click()
	# Take screenshot for verify
	driver[df.ssid[k]].save_screenshot('screenshot_' + str(k+1) + '.png')

for k in range(len(ssid)-1):
	driver[ssid[k]].quit

