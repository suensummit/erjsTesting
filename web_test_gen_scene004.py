from pandas import DataFrame
import csv
import time
import sys
import getopt
import random as rd

outputfile = str(sys.argv[1])
k = int(sys.argv[2])

with open(outputfile + '.csv', 'wb') as f:
	testbotwriter = csv.writer(f)
	#testbot_raw = list()
	testbotwriter.writerow(['ssid','uid','lo','act','cat','pid','pcat','paypid','qty','unit_price','eturec','oid','amt','ERCAMP','ERAD','flag'])
	for k in range(k):
		uidnum = rd.randint(1,999)
		before_cart = rd.randint(3,8)
		after_cart = 1
		i = 0
		while i < before_cart:
			ssid = "s%03d" %(k+1)
			uid = "u%03d" %(uidnum)
			lo = "1"
			act = "view"
			last_cat = rd.randint(0,9)
			cat = "catA%1d,catB%1d,catC%1d" %(rd.randint(0,9), rd.randint(0,9), last_cat)
			pid = "pC%1d_%02d" %(last_cat, rd.randint(0,9))
			pcat = ""
			paypid = ""
			qty = ""
			unit_price = ""
			eturec = "1"
			oid = ""
			amt = ""
			campid = rd.randint(0,9)
			ERCAMP = "camp%02d" %(campid)
			adid = rd.randint(0,9)
			ERAD = "ad%02d_%02d" %(campid, adid)
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD,0])
			i = i + 1
		# cart with probability
		if rd.random() < .8:
			j = 0
		else:
			j = 1
			pass
		while j < after_cart:
			act = "cart"
			pcat = cat
			paypid = pid
			cat = ""
			pid = ""
			nqty = rd.randint(1,5)
			qty = "%d" %(nqty)
			nprice = rd.randint(100,10000)
			unit_price = "%d" %(nprice)
			oid = ""
			amt = ""
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD,0])
			act = "order"
			oid = "o"+uid+time.strftime("%Y%m%d%H%M%S")
			amt = "%d" %(nqty*nprice)
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD,1])
			j = j + 1
