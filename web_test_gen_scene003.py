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
		before_cart = randint(2,5)
		after_cart = 1
		i = 0
		while i < before_cart:
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
			eturec = ""
			oid = ""
			amt = ""
			campid = randint(0,9)
			ERCAMP = "camp%02d" %(campid)
			adid = randint(0,99)
			ERAD = "ad%02d_%02d" %(campid, adid)
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD])
			i = i + 1
		j = 0
		while j < after_cart:
			ssid = "s%03d" %(k+1)
			uid = "u%03d" %(k+1)
			act = "cart"
			pcat = cat
			paypid = pid
			cat = ""
			pid = ""
			nqty = randint(1,5)
			qty = "%d" %(nqty)
			nprice = randint(100,10000)
			unit_price = "%d" %(nprice)
			oid = ""
			amt = ""
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD])
			act = "order"
			oid = "o"+uid+time.strftime("%Y%m%d%H%M%S")
			amt = "%d" %(nqty*nprice)
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD])
			j = j + 1
