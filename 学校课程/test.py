import re
from selenium import webdriver
import time,os

url='http://jxgl.hdu.edu.cn/jxrwcx.aspx'
file=open('kechengmingchen.txt','w')

def openwindow():
    driver = webdriver.Chrome(executable_path='C:\\Users\\assu\\PycharmProjects\\CTF\\学校课程\\chromedriver.exe')
    # driver.maximize_window()
    driver.get(url)
    for i in range(1,50000):
        yemian,yeshu=tiqu(driver.page_source)
        print("第{}页".format(yeshu[0]))
        # print(len(yemian),yemian,sep='\n')
        for j in range(1,len(yemian)):
            file.write(yemian[j][1]+'\n')

        time.sleep(1)
        if int(yeshu[0])>290:
            xpath = '//*[@id="DBGrid"]/tbody/tr[16]/td/a[{}]'.format(i%10+4)
        else:
            if i <11:
                xpath='//*[@id="DBGrid"]/tbody/tr[16]/td/a[{}]'.format(i)
            else:
                if i%10==0:
                    xpath = '//*[@id="DBGrid"]/tbody/tr[16]/td/a[{}]'.format(11)
                else:
                    xpath = '//*[@id="DBGrid"]/tbody/tr[16]/td/a[{}]'.format(i%10+1)
        try:
            select=driver.find_element_by_xpath(xpath=xpath)
            # print("要按的页数"+select.text,i)
            select.click()
        except:
            print("最后一页为第{}页".format(yeshu[0]))
            break

def tiqu(text):
    regax='<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'
    all_re=re.findall(regax,text)
    reg='<span>(.*?)</span>'
    arr_1=re.findall(reg,text)
    return all_re,arr_1

openwindow()
file.close()