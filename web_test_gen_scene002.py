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
		before_cart = rd.randint(2,5)
		after_cart = 1
		i = 0
		while i < before_cart:
			ssid = "s%03d" %(k+1)
			uid = "u%03d" %(uidnum)
			lo = "1"
			act = "view"
			last_cat = rd.randint(0,9)
			cat = "catA%1d,catB%1d,catC%1d" %(rd.randint(0,9), rd.randint(0,9), last_cat)
			pid = "pC%1d_%02d" %(last_cat, rd.randint(0,99))
			pcat = ""
			paypid = ""
			qty = ""
			unit_price = ""
			eturec = ""
			oid = ""
			amt = ""
			campid = rd.randint(0,9)
			ERCAMP = "camp%02d" %(campid)
			ERAD = "ad%02d_%02d" %(campid, rd.randint(0,99))
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD,0])
			i = i + 1
		j = 0
		while j < after_cart:
			lo = "1"
			act = "cart"
			pcat = cat
			paypid = pid
			cat = ""
			pid = ""
			qty = "%d" %(rd.randint(1,5))
			unit_price = "%d" %(rd.randint(100,10000))
			oid = ""
			amt = ""
			testbotwriter.writerow([ssid,uid,lo,act,cat,pid,pcat,paypid,qty,unit_price,eturec,oid,amt,ERCAMP,ERAD,1])
			j = j + 1

