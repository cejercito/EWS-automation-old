#!/usr/bin/env python
# vi: set ts=8 sts=4 sw=4 et:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException  
from time import sleep
import sys
import argparse
import time
import os

print r'''
                                     
                                      ____  _      _  ____   
                                     |  __|| |    | |/  __)               
                                     |  _] | | /\ | |\_\ _   PERFORMANCE         
                                     | [__ | \/  \/ |__ ) ) --------------                                                  
                            ____  _  |_ __|_\__/\__/(_____/____  _____  _  __  _   _
                           /    \| | | |_   _|/  \| \  / |/    \|_   _|| |/  \| \ | |
                          |  /\  | | | | | | | /\ |  \/  |  /\  | | |  | | /\ |  \| |
                          |  __  | |_| | | | | \/ |      |  __  | | |  | | \/ | |\  |
                          |_|  |_|\___/  |_|  \__/|_|\/|_|_|  |_| |_|  |_|\__/|_| \_|
                                
                          Christian Jay Ejercito          
                          Jane Lynel Buangjug
'''

ip = sys.argv[1]
execution = int(sys.argv[2])
browserr = sys.argv[3]

start1 = time.time()
count = 1
PATIENCE_TIME = 10


link_to_click = {
        '01'        : ['Status'     ,'//*[@id="Status-link"]/a'               ,'//*[@id="Supplies"]'], 
        '02'        : ['Settings'   ,'//*[@id="Settings-link"]/a'             ,'/html/body/div[2]/div[3]/div[3]/div[2]/div/div[2]/div[1]/div[1]/a/img'],
        '03'        : ['Device'     ,'//*[@id="Settings-Device-link"]/a'      ,'//*[@id="ScreenTimeout"]'],
	'04'        : ['Print'      ,'//*[@id="Settings-Print-link"]/a'       ,'//*[@id="PrintLayout"]'],
        '05'        : ['Paper'      ,'//*[@id="Settings-Paper-link"]/a'       ,'//*[@id="DefaultSource"]'],
        '06'        : ['Copy'       ,'//*[@id="Settings-Copy-link"]/a'        ,'//*[@id="CopyContentType"]'],
        '07'        : ['Fax'        ,'//*[@id="Settings-Fax-link"]/a'         ,'//*[@id="Fax"]'],
        '08'        : ['E-mail'     ,'//*[@id="Settings-Email-link"]/a'       ,'//*[@id="EmailDeviceUserid"]'],
        '09'        : ['FTP'        ,'//*[@id="Settings-Ftp-link"]/a'         ,'//*[@id="FtpFormat"]'],
        '10'        : ['USB Drive'  ,'//*[@id="Settings-FlashDrive-link"]/a'  ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[1]/div/div[3]/ul[1]/li/div[2]/table/thead/tr/th[1]/span'],
        '11'        : ['Network'    ,'//*[@id="Settings-Network-link"]/a'     ,'//html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[4]/div/div[3]/ul[1]/li[25]/div/a/span'],
        '12'        : ['Security'   ,'//*[@id="Settings-Security-link"]/a'    ,'//*[@id="PublicAccount"]'],
        '13'        : ['Report'     ,'//*[@id="Settings-Reports-link"]/a'     , '/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[1]/div/a'],
        '14'        : ['MenuSettingsPages' ,'//*[@id="Settings-Reports-link"]/a' ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[1]/div' ,'/html/body/div[1]/div[2]/div[4]/div/button[1]' ,'/html/body/div[1]/div[2]/div[4]/div/button[2]'],
        '15'        : ['DeviceStatistics' ,'//*[@id="Settings-Reports-link"]/a'   ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[2]/div' ,'//*[@id="ReportDeviceGroup-Breadcrumb"]' ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[2]/div' ,'/html/body/div[1]/div[2]/div[4]/ul/li/div/table[1]/tbody/tr/td[1]/b/font' ,'/html/body/div[1]/div[2]/div[4]/div/button'],
        '16'        : ['Address Book' ,'//*[@id="AddressBook-link"]/a'        ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[2]/div/div[3]/ul[1]/li/div/div[3]/table/tbody/tr'],
        '17'        : ['Shortcuts'  , '//*[@id="ShortcutsManagement-link"]/a' ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li/div/div[3]/table/thead/tr/th[2]'],
        '18'        : ['Bookmark Setup','//*[@id="BookmarkSetup-link"]/a'     ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[2]/div/ul/li/div/button'],
        '19'        : ['Apps'       ,'//*[@id="Applications-link"]/a'         ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[1]/div/div[3]/ul[1]/li[1]/div/button'],
        '20'        : ['Site Map'   ,'/html/body/div[2]/div[3]/div[2]/div[3]/div/a' ,'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[1]/div/div[3]/ul[1]/li/div/div/div[1]/div[1]/a']

         }


#sort by keys '01,02,03....'
link_to_click_sorted = sorted(link_to_click)

#open browser
if browserr == 'Chrome':
    browser = webdriver.Chrome()
elif browserr == 'Ie':
    browser = webdriver.Ie()
elif browserr == 'Firefox':
    browser = webdriver.Firefox()
else:
    print('\x1b[1;31;40m' + 'User Error!' + '\x1b[0m')
    print('\x1b[1;31;40m' + 'Example: python <python_link.py> <10.194.10.247> <1> <(Chrome,Firefox)>' + '\x1b[0m')
 
#result data
click_result_data = {}  

animation = "|/-\\"

while (count <= execution):
    print "Execution count %s/%s" % (count, execution)
    click_result_data[str(count)] = []
    wait                          = WebDriverWait(browser, PATIENCE_TIME)

    for x in link_to_click_sorted:

	link_element  = link_to_click[x][1]
        wait_element  = link_to_click[x][2]
   
        try:
            if link_to_click[x][0] == "Status":
                start_time = time.time()
                browser.get('http://' + ip)
		browser.find_element_by_xpath(link_element).click()
                end_time   = time.time()

                        	
            elif link_to_click[x][0] == "MenuSettingsPages":
                browser.find_element_by_xpath('//*[@id="Settings-Reports-link"]').click()
                start_time = time.time()
                browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[1]/div').click()
                wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[4]/ul/li/div/ul/li[2]/ul/li[1]/ul/li[1]')))
                end_time = time.time()
                sleep(1)
                browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div/button[2]').click()

            elif link_to_click[x][0] == "DeviceStatistics":
                browser.find_element_by_xpath('//*[@id="Settings-Reports-link"]').click()
                browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[2]/div').click()
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ReportDeviceGroup-Breadcrumb"]')))
                browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[2]/div').click()
                start_time = time.time()
                wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[4]/ul/li/div/table[1]/tbody/tr/td[1]/b/font')))
                end_time = time.time()
                sleep(1)
                browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div/button').click()

            elif link_to_click[x][0] == "Site Map":
                start_time = time.time()
                browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[3]/div/a/b/span').click()
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ReportNetworkGroup"]')))
                end_time = time.time()
                

            else:
                 try:
                     browser.find_element_by_xpath(link_element).click()
                     start_time = time.time()
                     wait.until(EC.presence_of_element_located((By.XPATH, wait_element)))
                     end_time = time.time()

                 except NoSuchElementException:
                     end_time = 0
                     start_time = 0
                     pass


        except TimeoutException as event:
            print ('\x1b[1;31;40m' + "Exception has been thrown: " + '\x1b[0m')
            end_time = 0
            start_time = 0
            pass

        # get elapsed time
        result     = end_time - start_time
        print "Result: \n %s = %s" % (link_to_click[x][0], ('\x1b[1;32;40m' + str(result)) + '\x1b[0m')
            
        click_result_data[str(count)].append(result)
        #Delay for 2 seconds
        time.sleep(2)
 
    count = count + 1

avg_data = {}
key_names = [link_to_click[i][0] for i in link_to_click_sorted]
for_csv_file = ','.join([link_to_click[i][0] for i in link_to_click_sorted])

for x,y in click_result_data.items():
   for_csv_file += "\n" + ','.join("%.2f" % (i) for i in y)
   for index in range(len(y)):
       if key_names[index] not in avg_data:
           avg_data[key_names[index]] = y[index]
       else:
           xsum = avg_data[key_names[index]]
           xsum += y[index]
           avg_data[key_names[index]] = xsum

avg_value = []
for key in key_names:
    avg_value.append(avg_data[key])

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print('\x1b[1;33;40m' + "csv has saved created into your file directory" + '\x1b[0m')


#print avg_value
for_csv_file += "\n" + ','.join("%.2f" % (i/execution) for i in avg_value)
print for_csv_file

file = open('file.csv', 'wb+')
file.write(for_csv_file + "\n")
file.close() 

browser.close()
