
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def driver_open():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (r"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36")
    driver = webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\Anaconda\phantomjs.exe', desired_capabilities=dcap)
    return driver
def get_content(driver,url):
    driver.get(url)
    time.sleep(30)
    content = driver.page_source.encode('utf-8')
    driver.close()
    soup = BeautifulSoup(content, 'lxml')
    return soup

def get_basic_info(soup):
    basic_info = soup.select('.baseInfo_model2017')

    zt = soup.select('.td-regStatus-value > p ')[0].text.replace("\n","").replace(" ","")
    basics = soup.select('.basic-td > .c8 > .ng-binding ')
    zzjgdm = basics[3].text
    tyshxydm = basics[7].text
    print (u'公司名称：'+company)
    print (u'公司状态：'+zt)
    # print basics
    print (u'组织机构代码：'+zzjgdm)
    print (u'统一社会信用代码：'+tyshxydm)

if __name__=='__main__':
    url = "http://www.tianyancha.com/company/2310290454"
    driver = driver_open()
    soup = get_content(driver, url)
    print(soup.body.text)
    print('----获取基础信息----')
    get_basic_info(soup)
