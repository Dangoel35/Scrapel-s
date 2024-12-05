from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import csv
from datetime import datetime

# Add meg a ChromeDriver pontos útvonalát
valasztasok = {}
datum1=datetime(1990,6,26)
datum2=datetime(1992,6,22)
datum3=datetime(1992,6,23)
datum4=datetime(1994,11,2)

datum5=datetime(1994,11,3)
datum6=datetime(1998,10,28)
datum7=datetime(1998,10,29)
datum8=datetime(2002,10,14)

datum9=datetime(2002,10,15)
datum10=datetime(2006,7,3)
datum11=datetime(2006,7,4)
datum12=datetime(2010,7,7)

datum13=datetime(2010,7,8)
datum14=datetime(2012,4,3)
datum15=datetime(2012,4,4)
datum16=datetime(2016,3,22)

datum17=datetime(2016,3,23)
datum18=datetime(2020,3,19)
datum19=datetime(2020,3,20)
datum20=datetime(2050,3,22)

valasztasok[(datum1,datum2)]="1990-1992"
valasztasok[(datum3,datum4)]="1992-1994"
valasztasok[(datum5,datum6)]="1994-1998"
valasztasok[(datum7,datum8)]="1998-2002"
valasztasok[(datum9,datum10)]="2002-2006"
valasztasok[(datum11,datum12)]="2006-2010"
valasztasok[(datum13,datum14)]="2010-2012"
valasztasok[(datum15,datum16)]="2012-2016"
valasztasok[(datum17,datum18)]="2016-2020"
valasztasok[(datum19,datum20)]="2020-"

service = Service('C:\\Users\\nagyd\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

# Hozd létre a Chrome webdriver példányt a Service osztállyal
driver = webdriver.Chrome(service=service)

# Példa: nyisd meg a Google-t
driver.get("https://www.slov-lex.sk/vyhladavanie-pravnych-predpisov?filter=1&typPredp=Zakon&vyhlasenie=5&orderByType=asc&delta=100")
time.sleep(10)
osoldal="https://www.slov-lex.sk/vyhladavanie-pravnych-predpisov?filter=1&typPredp=Zakon&vyhlasenie=5&orderByType=asc&delta=100"
csv_file='output_selenium.csv'
csv_file2='output2_selenium.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "year","source_name", "source_link", "electoral_cycle", "text_type", "complete_title","author", "date_introduced", "country", "language","no_document","date_published", "text"])
    lemo = True
    r = 0
    lo = 0
    while lemo:
        try:
            r +=1
            for i in range(2, 100):
                xpath = f'/html/body/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[2]/a'
                lo += 1
                try:
                    #print("Ez")
                    element = driver.find_element(By.XPATH, xpath)
                    print(f'Element at row {lo}: {element.text}')
                    #writer.writerow([lo, element.text])
                    wq=element.text
                    element.click()  # Kattint az elemre
                    time.sleep(2)
                    xyath = '/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[1]/div[2]/div[1]/table/tbody/tr/td[4]/img'
                    iframes = driver.find_elements(By.TAG_NAME, 'iframe')
                    driver.switch_to.frame(iframes[0])
                    #xcath = '/html/body/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/ul/li[3]/a'
                    gatya = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[1]/div[2]/div[1]/table/tbody/tr/td[4]/img')
                    gatya.click()
                    time.sleep(2)
                    xvat ='/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/a/span'
                    gat = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/a/span')
                    gat.click()
                    time.sleep(2)
                    szomi = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[1]/div[1]')
                    terem=szomi.text[4:8]
                    torvnum=szomi.text[0:3]
                    remesz=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[3]')
                    fulltext=remesz.text
                    fulltext=fulltext.replace("\n", " ")
                    ret =driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[2]/button[1]')
                    ret.click()
                    rem=driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]')
                    date_intro= rem.text
                    datrum=datetime(int(date_intro[6:11]), int(date_intro[3:5]), int(date_intro[0:2]))
                    print(datrum)

                    rimo=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[5]/td[2]')
                    author=rimo.text
                    zer=datetime(int(author[6:11]), int(author[3:5]), int(author[0:2]))
                    weres=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[6]/td[2]')
                    autho=weres.text
                    szak = ""
                    for (ii,kk),ll in  valasztasok.items():
                        if ii <= datrum and datrum <= kk:
                            szak=ll
                    print(szak)
                    writer.writerow([lo, terem,"slov-lex.sk", driver.current_url, szak, "law", wq, autho, datrum,"Slovak Republic", "Slovakian",torvnum,zer , fulltext])
                    driver.get(osoldal)
                    time.sleep(2)
                except:
                    print(1)
            ele = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/ul/li[3]/a')
            ele.click()
            osoldal=driver.current_url
            if r == 50:
                lemo = False
        except:
            lemo=False


driver.quit()