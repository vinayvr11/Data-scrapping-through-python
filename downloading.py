from bs4 import BeautifulSoup as soup
import urllib
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

take = input('ENTER THE DISTRICT- ')
polling_list = []
url = urllib.request.urlopen('http://ceoharyana.nic.in/?module=draftroll')
sop = soup(url,'html.parser')

#Find all the options 
sop1 = sop('option')
l = []
for n in sop1:
    l.append(n.get('value') + ' ' + n.get_text())
#district ka naam check karne ke liye hai ya nahi
for m in range(1,len(l)):
    if take in l[m]:
        index = m
        #Select the district column for access the AC        
driver = webdriver.Firefox()
driver.get('http://ceoharyana.nic.in/?module=draftroll')

select = Select(driver.find_element_by_name('district'))

select.select_by_index(index)

wait(driver,4).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ac"]/option[2]')))
time.sleep(2)
element = driver.find_element_by_name('ac')
all_options = element.find_elements_by_tag_name("option")
l1 = []
for option in all_options:
    l1.append(option.get_attribute("value"))     

del l1[0]
AC = len(l1)
  #Wait web driver for opening the polling station's
for assem in range(1,AC+1):
    select_AC = Select(driver.find_element_by_name('ac'))
    select_AC.select_by_index(assem)
    
    wait(driver,4).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ps"]/option[2]')))

    se = driver.find_element_by_name('ps')
    se1 = se.find_elements_by_tag_name('option')
    for m in se1:
        polling_list.append(m.get_attribute('value'))
    el = driver.implicitly_wait(4)
    time.sleep(2)
for ur in range(1,len(polling_list)):
    if polling_list[ur] == '0':
        continue
    
    a1,a2 = polling_list[ur].split('-')
    name = polling_list.index(polling_list[ur])
    
    if len(a1) == 1:
        
        make_url = 'http://ceoharyana.nic.in/docs/election/draftroll2019/CMB'+a2+'/CMB0'+a2+'000'+a1+'.PDF'
        download = urllib.request.urlopen(make_url)
        with  open('%s.pdf' % name, 'wb') as f:
            f.write(download.read())
        time.sleep(4)
    elif len(a1) == 2:
        
        makee_url1 = 'http://ceoharyana.nic.in/docs/election/draftroll2019/CMB'+a2+'/CMB0'+a2+'00'+a1+'.PDF'
        download1 = urllib.request.urlopen(makee_url1)
        with open('%s.pdf' % name,'wb') as f1:
            f1.write(download1.read())
        time.sleep(4)
    elif len(a1) == 3:
        make_url2 = 'http://ceoharyana.nic.in/docs/election/draftroll2019/CMB'+a2+'/CMB0'+a2+'0'+a1+'.PDF'
        download2 = urllib.request.urlopen(make_url2)
        with open('%s.pdf' % name,'wb') as f2:
            f2.write(download2.read()) 
        time.sleep(4)