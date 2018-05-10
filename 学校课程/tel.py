import re
from selenium import webdriver
import time,os
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

url='http://2521596110.qzone.qq.com'
driver = webdriver.Chrome(executable_path='C:\\Users\\assu\\PycharmProjects\\CTF\\学校课程\\chromedriver.exe')

def openwindow():
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    xpath='//*[@id="switcher_plogin"]'
    # print(driver.page_source)
    try:
        driver.switch_to_frame("login_frame")
        driver.find_element_by_id("img_out_491565693").click()
    except:
        print("失败")
    time.sleep(1)

def opendongtai():
    xpath='//*[@id="friendship_promote_layer"]/table/tbody/tr[1]/td[2]/a'
    # ActionChains(driver).move_by_offset(400, 600).double_click()
    driver.find_element_by_xpath(xpath).click()
    try:
        driver.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[5]/a').click()
    except:
        print("没找到")

    print(driver.page_source)
    fanye()

def fanye(x=3):
    name='pager_num_{}_{}'
    time.sleep(3)
    for i in range(x):
        driver.find_element_by_id(name.format(i,i+2)).click()

def fenxi():
    pass
openwindow()
opendongtai()