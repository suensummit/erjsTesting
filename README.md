# ER SaaS End-to-End Test
---

Welcome to [Etu Recommander SaaS](http://54.169.252.99/admin/_dashboard.html)! This document will help you to use `python + selenium + phantomjs` simulating the user's behavior and verify the whole software functionality step-by-step.

---

# Environment Setup

- ## Manually testing locally (OSX)

	- python

	```
	### install homebrew first
	$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	$ export PATH=/usr/local/bin:/usr/local/sbin:$PATH

	### install python via homebrew
	$ brew install python
	```

	- selenium & pandas

	```
	$ pip install selenium pandas
	```

	- firefox (default browser driver in selenium)

	```
	### install brew-cask first
	$ brew tap phinze/homebrew-cask
	$ brew install brew-cask

	### install firefox via brew-cask
	$ brew cask install firefox
	```

	- phantomjs (quick and lightweight alternative)

	```
	$ brew update && brew install phantomjs
	```

- ## Remote testing automatically (CentOS@209)

	- python

		Just using the default version for convenience.

	- phantomjs

	```
	### download phantomjs
	[root@master ~]# curl -O https://phantomjs.googlecode.com/files/phantomjs-1.9.2-linux-x86_64.tar.bz2
  	% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	100 12.6M  100 12.6M    0     0  1048k      0  0:00:12  0:00:12 --:--:-- 2620k
	### extract directory
	[root@master ~]# tar xvf 	phantomjs-1.9.2-linux-x86_64.tar.bz2

	### copy binary to bin folder
	[root@master ~]# cp phantomjs-1.9.2-linux-x86_64/bin/phantomjs /usr/local/bin

	### verify your installation: Hello, world!
	[root@master ~]# curl -O https://raw.githubusercontent.com/ariya/phantomjs/master/examples/hello.js
  	% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
  	0    46    0    46    0     0    108      0 --:--:-- --:--:-- --:--:--   200
	[root@master ~]# phantomjs hello.js
	Hello, world!
	[root@master ~]#
	```

	- selenium

	```
	[root@master ~]# pip install selenium
	```

 	- pandas

	```
	[root@master ~]# yum install gcc-gfortran
	[root@master ~]# yum install libgfortran
	[root@master ~]# yum install lapack
	[root@master ~]# yum install gcc-c++
	[root@master ~]# pip install numpy
	[root@master ~]# pip install pandas
	```

---

# Test Site Preparation

[PreDomain](http://210.63.38.209:8099/test_entry.html)

[Test site](http://210.63.38.209:8099/test.html)

---

# Test Data Preparation

- Input:

	- csv files `web_test_scene00{1-4}.csv` which describe actions for each robot.
	- python script `web_saas.py` which control the robots.

	Put them all together under your test project directory.

	```
	## or simply clone from github
	$ git clone git@github.com:etusolution/erjsTesting.git
	```

- Format:

	| Field | Type | Description |
	|---|---|---|
	| date | timestamp | Date of action |
	| Time | timestamp | Time of action |
	| ssid | string | Session ID |
	| uid | string | User ID |
	| eruid | string | Tracking UID |
	| lo | boolean | Login flag |
	| act | string | Action |
	| cat | string | Category (view) |
	| pid | string | Product ID (view) |
	| pcat | string | Category (payment) |
	| paypid | string | Product ID (payment) |
	| qty | int | Order quantity |
	| unit_price | int | Price of each product |
	| eturec | int | rec tag |
	| oid | string | Order ID |
	| amt | int | Total amount of payment |
	| ERCAMP | string | Campaign ID |
	| ERAD | string | Advertising ID |

	- Example: [web_test_scene001.csv](https://github.com/suensummit/erjsTesting/blob/gh-pages/web_test_scene001.csv)

	| ssid | uid  | lo | act  | cat    | pid   | pcat   | paypid | qty | unit_price | eturec | oid | amt | ERCAMP | ERAD |        |         |
	|------|------|----|------|--------|-------|--------|--------|-----|------------|--------|-----|-----|--------|------|--------|---------|
	| s001 |      | 0  | view | "catA4 ,catB7 ,catC8" | pC8_83 |     |            |        |     |     |        |      | camp06 | ad06_32 |
	| s001 |      | 0  | view | "catA0 ,catB3 ,catC0" | pC0_06 |     |            |        |     |     |        |      | camp05 | ad05_05 |
	| s001 |      | 0  | view | "catA2 ,catB7 ,catC0" | pC0_26 |     |            |        |     |     |        |      | camp04 | ad04_98 |
	| s001 | u001 | 1  | view | "catA4 ,catB2 ,catC5" | pC5_19 |     |            |        |     |     |        |      | camp09 | ad09_12 |
	| s001 | u001 | 1  | view | "catA7 ,catB1 ,catC8" | pC8_54 |     |            |        |     |     |        |      | camp08 | ad08_53 |
	| s002 |      | 0  | view | "catA8 ,catB7 ,catC0" | pC0_36 |     |            |        |     |     |        |      | camp09 | ad09_35 |
	| s002 |      | 0  | view | "catA9 ,catB9 ,catC4" | pC4_99 |     |            |        |     |     |        |      | camp08 | ad08_22 |
	| s002 |      | 0  | view | "catA6 ,catB8 ,catC6" | pC6_23 |     |            |        |     |     |        |      | camp09 | ad09_66 |
	| s002 |      | 0  | view | "catA8 ,catB5 ,catC0" | pC0_73 |     |            |        |     |     |        |      | camp08 | ad08_77 |
	| s002 | u002 | 1  | view | "catA6 ,catB7 ,catC1" | pC1_33 |     |            |        |     |     |        |      | camp02 | ad02_68 |
	| s002 | u002 | 1  | view | "catA5 ,catB6 ,catC3" | pC3_72 |     |            |        |     |     |        |      | camp05 | ad05_42 |
	| s002 | u002 | 1  | view | "catA0 ,catB8 ,catC4" | pC4_88 |     |            |        |     |     |        |      | camp06 | ad06_53 |
	| s003 |      | 0  | view | "catA9 ,catB5 ,catC5" | pC5_84 |     |            |        |     |     |        |      | camp01 | ad01_34 |
	| s003 |      | 0  | view | "catA9 ,catB8 ,catC7" | pC7_54 |     |            |        |     |     |        |      | camp06 | ad06_36 |
	| s003 |      | 0  | view | "catA7 ,catB6 ,catC4" | pC4_40 |     |            |        |     |     |        |      | camp02 | ad02_78 |
	| s003 |      | 0  | view | "catA6 ,catB0 ,catC0" | pC0_70 |     |            |        |     |     |        |      | camp04 | ad04_58 |
	| s003 |      | 0  | view | "catA4 ,catB3 ,catC4" | pC4_41 |     |            |        |     |     |        |      | camp01 | ad01_11 |
	| s003 |      | 0  | view | "catA5 ,catB8 ,catC8" | pC8_00 |     |            |        |     |     |        |      | camp06 | ad06_01 |
	| s003 | u003 | 1  | view | "catA7 ,catB2 ,catC8" | pC8_11 |     |            |        |     |     |        |      | camp00 | ad00_46 |
	| s003 | u003 | 1  | view | "catA9 ,catB3 ,catC2" | pC2_61 |     |            |        |     |     |        |      | camp05 | ad05_70 |
	| s003 | u003 | 1  | view | "catA3 ,catB8 ,catC0" | pC0_53 |     |            |        |     |     |        |      | camp04 | ad04_82 |
	| s004 |      | 0  | view | "catA7 ,catB2 ,catC3" | pC3_36 |     |            |        |     |     |        |      | camp06 | ad06_93 |
	| s004 |      | 0  | view | "catA6 ,catB3 ,catC5" | pC5_88 |     |            |        |     |     |        |      | camp01 | ad01_66 |
	| s004 |      | 0  | view | "catA7 ,catB5 ,catC6" | pC6_28 |     |            |        |     |     |        |      | camp09 | ad09_02 |
	| s004 |      | 0  | view | "catA8 ,catB9 ,catC3" | pC3_25 |     |            |        |     |     |        |      | camp00 | ad00_05 |
	| s004 | u004 | 1  | view | "catA8 ,catB7 ,catC2" | pC2_36 |     |            |        |     |     |        |      | camp07 | ad07_00 |
	| s004 | u004 | 1  | view | "catA4 ,catB5 ,catC5" | pC5_88 |     |            |        |     |     |        |      | camp03 | ad03_20 |
	| s005 |      | 0  | view | "catA0 ,catB6 ,catC2" | pC2_99 |     |            |        |     |     |        |      | camp03 | ad03_87 |
	| s005 |      | 0  | view | "catA1 ,catB1 ,catC2" | pC2_66 |     |            |        |     |     |        |      | camp06 | ad06_44 |
	| s005 |      | 0  | view | "catA2 ,catB6 ,catC7" | pC7_59 |     |            |        |     |     |        |      | camp03 | ad03_06 |
	| s005 |      | 0  | view | "catA7 ,catB8 ,catC4" | pC4_32 |     |            |        |     |     |        |      | camp03 | ad03_43 |
	| s005 | u005 | 1  | view | "catA2 ,catB5 ,catC7" | pC7_72 |     |            |        |     |     |        |      | camp05 | ad05_87 |
	| s005 | u005 | 1  | view | "catA8 ,catB9 ,catC3" | pC3_23 |     |            |        |     |     |        |      | camp01 | ad01_82 |
	| s005 | u005 | 1  | view | "catA4 ,catB1 ,catC1" | pC1_98 |     |            |        |     |     |        |      | camp02 | ad02_81 |
	| s005 | u005 | 1  | view | "catA1 ,catB6 ,catC9" | pC9_51 |     |            |        |     |     |        |      | camp02 | ad02_42 |
	| s006 |      | 0  | view | "catA5 ,catB4 ,catC0" | pC0_55 |     |            |        |     |     |        |      | camp06 | ad06_60 |
	| s006 |      | 0  | view | "catA3 ,catB2 ,catC4" | pC4_31 |     |            |        |     |     |        |      | camp06 | ad06_60 |
	| s006 |      | 0  | view | "catA2 ,catB0 ,catC7" | pC7_81 |     |            |        |     |     |        |      | camp02 | ad02_27 |
	| s006 |      | 0  | view | "catA2 ,catB9 ,catC1" | pC1_83 |     |            |        |     |     |        |      | camp09 | ad09_72 |
	| s006 |      | 0  | view | "catA3 ,catB8 ,catC2" | pC2_30 |     |            |        |     |     |        |      | camp08 | ad08_21 |
	| s006 |      | 0  | view | "catA8 ,catB7 ,catC3" | pC3_40 |     |            |        |     |     |        |      | camp00 | ad00_90 |
	| s006 |      | 0  | view | "catA5 ,catB0 ,catC6" | pC6_98 |     |            |        |     |     |        |      | camp08 | ad08_27 |
	| s006 |      | 0  | view | "catA8 ,catB1 ,catC4" | pC4_71 |     |            |        |     |     |        |      | camp05 | ad05_11 |
	| s006 | u006 | 1  | view | "catA4 ,catB4 ,catC6" | pC6_36 |     |            |        |     |     |        |      | camp06 | ad06_31 |
	| s006 | u006 | 1  | view | "catA8 ,catB2 ,catC5" | pC5_67 |     |            |        |     |     |        |      | camp05 | ad05_84 |
	| s007 |      | 0  | view | "catA9 ,catB1 ,catC1" | pC1_12 |     |            |        |     |     |        |      | camp09 | ad09_24 |
	| s007 |      | 0  | view | "catA7 ,catB9 ,catC4" | pC4_83 |     |            |        |     |     |        |      | camp06 | ad06_73 |
	| s007 |      | 0  | view | "catA8 ,catB4 ,catC3" | pC3_20 |     |            |        |     |     |        |      | camp02 | ad02_40 |
	| s007 |      | 0  | view | "catA5 ,catB1 ,catC9" | pC9_89 |     |            |        |     |     |        |      | camp08 | ad08_36 |
	| s007 |      | 0  | view | "catA5 ,catB2 ,catC8" | pC8_48 |     |            |        |     |     |        |      | camp06 | ad06_90 |
	| s007 |      | 0  | view | "catA9 ,catB9 ,catC0" | pC0_64 |     |            |        |     |     |        |      | camp00 | ad00_50 |
	| s007 | u007 | 1  | view | "catA3 ,catB4 ,catC3" | pC3_37 |     |            |        |     |     |        |      | camp02 | ad02_89 |
	| s007 | u007 | 1  | view | "catA5 ,catB4 ,catC9" | pC9_94 |     |            |        |     |     |        |      | camp08 | ad08_89 |
	| s007 | u007 | 1  | view | "catA9 ,catB1 ,catC7" | pC7_45 |     |            |        |     |     |        |      | camp04 | ad04_55 |
	| s007 | u007 | 1  | view | "catA0 ,catB3 ,catC8" | pC8_00 |     |            |        |     |     |        |      | camp03 | ad03_50 |
	| s007 | u007 | 1  | view | "catA9 ,catB9 ,catC4" | pC4_70 |     |            |        |     |     |        |      | camp07 | ad07_83 |
	| s008 |      | 0  | view | "catA1 ,catB2 ,catC4" | pC4_89 |     |            |        |     |     |        |      | camp06 | ad06_39 |
	| s008 |      | 0  | view | "catA4 ,catB6 ,catC6" | pC6_88 |     |            |        |     |     |        |      | camp07 | ad07_08 |
	| s008 |      | 0  | view | "catA8 ,catB6 ,catC8" | pC8_49 |     |            |        |     |     |        |      | camp00 | ad00_80 |
	| s008 |      | 0  | view | "catA1 ,catB0 ,catC7" | pC7_56 |     |            |        |     |     |        |      | camp06 | ad06_96 |
	| s008 |      | 0  | view | "catA8 ,catB1 ,catC3" | pC3_29 |     |            |        |     |     |        |      | camp07 | ad07_58 |
	| s008 |      | 0  | view | "catA1 ,catB5 ,catC1" | pC1_87 |     |            |        |     |     |        |      | camp02 | ad02_18 |
	| s008 |      | 0  | view | "catA9 ,catB7 ,catC1" | pC1_61 |     |            |        |     |     |        |      | camp01 | ad01_44 |
	| s008 | u008 | 1  | view | "catA9 ,catB1 ,catC6" | pC6_39 |     |            |        |     |     |        |      | camp04 | ad04_66 |
	| s008 | u008 | 1  | view | "catA1 ,catB8 ,catC6" | pC6_24 |     |            |        |     |     |        |      | camp04 | ad04_98 |
	| s009 |      | 0  | view | "catA9 ,catB3 ,catC1" | pC1_43 |     |            |        |     |     |        |      | camp00 | ad00_55 |
	| s009 |      | 0  | view | "catA0 ,catB9 ,catC0" | pC0_47 |     |            |        |     |     |        |      | camp05 | ad05_64 |
	| s009 |      | 0  | view | "catA0 ,catB6 ,catC4" | pC4_05 |     |            |        |     |     |        |      | camp09 | ad09_39 |
	| s009 |      | 0  | view | "catA2 ,catB2 ,catC2" | pC2_41 |     |            |        |     |     |        |      | camp05 | ad05_06 |
	| s009 |      | 0  | view | "catA5 ,catB5 ,catC0" | pC0_52 |     |            |        |     |     |        |      | camp00 | ad00_71 |
	| s009 | u009 | 1  | view | "catA5 ,catB1 ,catC5" | pC5_72 |     |            |        |     |     |        |      | camp00 | ad00_89 |
	| s009 | u009 | 1  | view | "catA5 ,catB7 ,catC1" | pC1_05 |     |            |        |     |     |        |      | camp07 | ad07_38 |
	| s009 | u009 | 1  | view | "catA1 ,catB4 ,catC3" | pC3_71 |     |            |        |     |     |        |      | camp00 | ad00_76 |
	| s009 | u009 | 1  | view | "catA8 ,catB3 ,catC1" | pC1_83 |     |            |        |     |     |        |      | camp08 | ad08_10 |
	| s010 |      | 0  | view | "catA3 ,catB8 ,catC3" | pC3_12 |     |            |        |     |     |        |      | camp01 | ad01_56 |
	| s010 |      | 0  | view | "catA5 ,catB2 ,catC2" | pC2_22 |     |            |        |     |     |        |      | camp02 | ad02_18 |
	| s010 |      | 0  | view | "catA6 ,catB1 ,catC7" | pC7_22 |     |            |        |     |     |        |      | camp05 | ad05_36 |
	| s010 | u010 | 1  | view | "catA9 ,catB9 ,catC6" | pC6_71 |     |            |        |     |     |        |      | camp00 | ad00_16 |
	| s010 | u010 | 1  | view | "catA5 ,catB0 ,catC0" | pC0_64 |     |            |        |     |     |        |      | camp03 | ad03_45 |

- ## Usage

	```
	### run the python script follow by input filename under project folder
	$ python web_saas.py web_test_scene001.csv
	```

- ## Lookup Python Script Step-by-step

	- Import dependency libraries
	```
	from selenium import webdriver
	from pandas import *
	import csv
	import time
	import sys
	import getopt
	```

	- Load test csv data from input argv for different scenari
	```
	inputfile = str(sys.argv[1])
	with open(inputfile, 'rb') as f:
		reader = csv.reader(f)
		testbot_raw = list(reader)
	```

	- Build up well-structured robot dataframe
	```
	testbot = sorted(testbot_raw, key=lambda testbot_raw: testbot_raw[2])
	df = DataFrame(testbot, columns = testbot[len(testbot)-1])
	```

	- Target url setting and initializing web browser driver(s)
	```
	url = "http://localhost/"
	#url = "file:///Users/summitsuen/Documents/erjsTesting/index.html"
	#url = "https://suensummit.github.io/erjsTesting/"

	# initialize drivers
	driver = {}
	k = 0
	ssid = df.ssid.unique()
	while k < len(ssid)-1:
		key = ssid[k]
		value = webdriver.PhantomJS()
		#value = webdriver.Firefox()
		driver[key] = value
		k += 1
	```

	- Send actions from robot dataframe
	```
	# send actions from testbot
	for k in range(len(df)-2):
		driver[df.ssid[k]].get(url)
		driver[df.ssid[k]].find_element_by_id('agroup').send_keys("ER")
		driver[df.ssid[k]].find_element_by_id('acid').send_keys("webtesting")
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
		driver[df.ssid[k]].find_element_by_id('aercamp').send_keys(df.ERCAMP[k])
		driver[df.ssid[k]].find_element_by_id('aerad').send_keys(df.ERAD[k])
		#print 'It is the ' + str(k+1) + 'th testbot\n'
		driver[df.ssid[k]].find_element_by_id('custom-click').click()
		# Take screenshot for verify
		#driver[df.ssid[k]].save_screenshot('screenshot_' + str(k+1) + '.png')

	# close jobs
	for k in range(len(ssid)-1):
		driver[ssid[k]].quit
	```

---
2015-03-02 last edited by [Summit Suen](https://github.com/suensummit)
