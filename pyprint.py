# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os
import time

# change to test folder
os.chdir('/Users/easonchan/test')

#website_with_logins = "http://service.moj.gov.tw/lawer/associList.asp?associName=%A5x%A5_%AB%DF%AEv%A4%BD%B7|"
website = []
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%A5x%A4%A4%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%A5x%A5_%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%A5x%AAF%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%A5x%ABn%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%A9y%C4%F5%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%AA%E1%BD%AC%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%ABn%A7%EB%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%AB%CC%AAF%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%AD]%AE%DF%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%AE%E7%B6%E9%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%B0%AA%B6%AF%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%B0%F2%B6%A9%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%B6%B3%AAL%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%B7s%A6%CB%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%B9%C5%B8q%AB%DF%AEv%A4%BD%B7|')
website.append('http://service.moj.gov.tw/lawer/associList.asp?associName=%B9%FC%A4%C6%AB%DF%AEv%A4%BD%B7|')
websitename = ['taichung','taipei','taidung','tainan','ilan','hualien','nantao','pintung','miaoli','taoyuan','kaohsiung','keelung','yunlin','hsinchu','chiayi','chunghwa']

driver = webdriver.Chrome()
i = 10
for link in website[-3:]:
    driver.get( str(link) )
    ps = driver.page_source
    soup = bs(ps)
    souptext = soup.getText()
    tmp = souptext.replace('\n',',')
    tmp = tmp.replace(',,,',',')
    tmp = tmp.replace(',,',',')
    tmp = tmp[:-15]
    tmp = tmp[292:]
    namelist = tmp.split(',')
    for name in namelist:
        f = open(websitename[i] +'_' + name + '.txt',"w+")
        isfound = True
        try:
            driver.find_element_by_partial_link_text(name)
        except:
            print 'Failed at:' + name
            isfound = False
        if(isfound):
            tmp1 = driver.find_element_by_partial_link_text(name)
            tmp1.click()
            tmp2 = driver.page_source
            time.sleep(1)
            f.write(unicode(tmp2).encode('utf8'))
            driver.back()
            time.sleep(1)
        f.close()
    
    print websitename[i] + 'finished'
    i += 1
        



    


