from pandas import DataFrame
import csv
import time
import sys
import getopt
from random import randint

outputfile = str(sys.argv[1])
k = int(sys.argv[2])

with open(outputfile + '.csv', 'wb') as f:
	testbotwriter = csv.writer(f)
	#testbot_raw = list()
	testbotwriter.writerow(['ssid','uid','lo','act','cat','pid','pcat','paypid','qty','unit_price','eturec','oid','amt','ERCAMP','ERAD'])
	for k in range(k):
		before_login = randint(3,8)
		after_login = randint(2,5)
		i = 0
		while i < before_login:
			ssid = "s%03d" %(k+1)
			uid = ""
			#uid = "u%03d" %(k+1)
			lo = "0"
			act = "view"
			last_cat = randint(0,9)
			cat = "catA%1d,catB%1d,catC%1d" %(randint(0,9), randint(0,9), last_cat)
			pid = "pC%1d_%02d" %(last_cat, randint(0,99))
			pcat = ""
			paypid = ""
			qty = ""
			unit_price = ""
			eturec = ""
			oid = ""
			amt = ""
			campid = randint(0,9)
			ERCAMP = "camp%02d" %(campid)
			ERAD = "ad%02d_%02d" %(campid, randint(0,99))
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD])
			i = i + 1
		j = 0
		while j < after_login:
			ssid = "s%03d" %(k+1)
			uid = "u%03d" %(k+1)
			lo = "1"
			act = "view"
			last_cat = randint(0,9)
			cat = "catA%1d,catB%1d,catC%1d" %(randint(0,9), randint(0,9), last_cat)
			pid = "pC%1d_%02d" %(last_cat, randint(0,99))
			pcat = ""
			paypid = ""
			qty = ""
			unit_price = ""
			oid = ""
			amt = ""
			campid = randint(0,9)
			ERCAMP = "camp%02d" %(campid)
			ERAD = "ad%02d_%02d" %(campid, randint(0,99))
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD])
			j = j + 1

