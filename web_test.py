from selenium import webdriver
import csv

# set test sample ec site
#url = "https://"
url = "https://duckduckgo.com/"

#for x in testbot:
#	for action in testbot(x).act_list:
a = {}
k = 0
while k < 3:
    key = k
    value = webdriver.Firefox()
    a[key] = value 
    k += 1

#driver + i = webdriver.Firefox()
#driver1 = webdriver.PhantomJS()
a[0].get(url)
a[1].get(url)
a[2].get(url)
#driver2 = webdriver.PhantomJS()
#driver2.get(url)
#driver3 = webdriver.PhantomJS()
#driver3.get(url)
#driver.get(url)
#driver.find_element_by_id().send_keys()
#driver.find_element_by_id().click()
a[0].quit()
a[1].quit()
a[2].quit()
#driver1.quit()
#driver2.quit()
#driver3.quit()
