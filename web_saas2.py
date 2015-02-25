from selenium import webdriver
from pandas import *
import csv
import time
import sys
import getopt

# load test data

inputfile = str(sys.argv[1])
with open(inputfile, 'rb') as f:
#with open('web_test_cat.csv', 'rb') as f:
#with open('web_test_src.csv', 'rb') as f:
#with open('web_test_funnel.csv', 'rb') as f:
#with open('web_test_camp.csv', 'rb') as f:
	reader = csv.reader(f)
	testbot_raw = list(reader)

testbot = sorted(testbot_raw, key=lambda testbot_raw: testbot_raw[2])
df = DataFrame(testbot, columns = testbot[len(testbot)-1])

# set test sample ec url
preurl = "http://210.63.38.209:8099/test_entry.html"
url = "http://210.63.38.209:8099/test.html"

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
	driver[df.ssid[k]].get(preurl)
	driver[df.ssid[k]].find_element_by_link_text('TEST').click()
	driver[df.ssid[k]].find_element_by_id('agroup').send_keys("etusolution")
	driver[df.ssid[k]].find_element_by_id('acid').send_keys("etusolutionrec")
	driver[df.ssid[k]].find_element_by_id('auid').send_keys(df.uid[k])
	if df.lo[k] == '0':
		driver[df.ssid[k]].find_element_by_id('auid').send_keys("")
		pass
	driver[df.ssid[k]].find_element_by_id('aact').send_keys(df.act[k])
	driver[df.ssid[k]].find_element_by_id('acat').send_keys(df.cat[k])
	driver[df.ssid[k]].find_element_by_id('apid').send_keys(df.pid[k])
	driver[df.ssid[k]].find_element_by_id('apcat').send_keys(df.pcat[k])
	driver[df.ssid[k]].find_element_by_id('apaypid').send_keys(df.paypid[k])
	driver[df.ssid[k]].find_element_by_id('aunit_price').send_keys(df.unit_price[k])
	#driver[df.ssid[k]].find_element_by_id('apmk').send_keys(df.pmk[k])
	driver[df.ssid[k]].find_element_by_id('aqty').send_keys(df.qty[k])
	driver[df.ssid[k]].find_element_by_id('aeturec').send_keys(df.eturec[k])
	driver[df.ssid[k]].find_element_by_id('aoid').send_keys(df.oid[k])
	driver[df.ssid[k]].find_element_by_id('aercamp').send_keys(df.ERCAMP[k])
	driver[df.ssid[k]].find_element_by_id('aerad').send_keys(df.ERAD[k])
	#print 'It is the ' + str(k+1) + 'th testbot\n'
	#time.sleep(1)
	driver[df.ssid[k]].find_element_by_id('custom-click').click()
	# Take screenshot for verify
	#driver[df.ssid[k]].save_screenshot('screenshot_' + str(k+1) + '.png')

for k in range(len(ssid)-1):
	driver[ssid[k]].quit()

