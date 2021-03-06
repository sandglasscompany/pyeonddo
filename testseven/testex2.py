import time as t
from selenium import webdriver
import pandas as pd


cf = open("emart_spot.csv", "w")
# cf.write("name,price,img,event,store_name\n")
browser = webdriver.Chrome()

browser.get("https://www.emart24.co.kr/introduce2/findBranch.asp")
# browser.execute_script("window.scrollTo(0, 1000)")
# infoK = {
#     3:'약',
#     6:'ATM',
#     15:'와인',
#     8:'로또',
#     4:'택배',
#     18:'베이커리',
# }


row = []
# 마지막 페이지 확인
last = browser.find_element_by_css_selector('.bgNone:last-child').get_attribute('href').lstrip("javascript:goPage('").rstrip("');")
# print(int(last))
for k in range(1,int(last)+1):
# for k in range(1,10):
    for i in range(1,6):
        atm = False
        medi = False
        wine = False
        lotto = False
        deliver = False
        bakery = False
        store = browser.find_element_by_css_selector('#skipCont > div.section > div.find_listArea.openList > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(1) > strong')
        addrInfo = browser.find_element_by_css_selector('#skipCont > div.section > div.find_listArea.openList > table > tbody > tr:nth-child('+str(i)+') > td.txtLeft > p:nth-child(1)').text.split(" | ")
        addr = addrInfo[0]
        time = addrInfo[1].lstrip("영업시간 : ")
        for j in range(1,20):
            info = browser.find_element_by_css_selector('#skipCont > div.section > div.find_listArea.openList > table > tbody > tr:nth-child('+str(i)+') > td.txtLeft > p.find_listSelect_Img > img:nth-child('+str(j)+')').get_attribute('src')
            if '_on' in info:
                if j in [3,4,6,8,15,18]:
                    print(j)
                if j==6:
                    atm = True
                elif j==3:
                    medi = True
                elif j==15:
                    wine = True
                elif j==8:
                    lotto = True
                elif j==4:
                    deliver = True
                elif j==18:
                    bakery = True
        row.append({
            'store' : store.text,
            'addr' : addr,
            'time' : time,
            'atm' : atm,
            'medicine' : medi,
            'wine' : wine,
            'lotto' : lotto,
            'charge' : False,
            'cigarette' : False,
            'bakery' : bakery,
            'delivery' : deliver,
        })
    print(row)
    print('*'*100)
    t.sleep(0.5)
    nextpage = browser.find_element_by_css_selector('#skipCont > div.section > div.find_listArea.openList > div > a.next.bgNone')
    nextpage.click()    

df=pd.DataFrame(row)
df.to_csv("test.csv", header=True)