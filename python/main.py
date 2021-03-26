import time

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib
import datetime

# url 2020년 1월1일부터 2020년 12월 31일 까지 설정한 상태 (총 252일)
targetUrl = "https://finance.yahoo.com/quote/RIOT/history?period1=1577836800&period2=1609372800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
localhost = "http://127.0.0.1:8080/"

response = requests.get(targetUrl)

if response.status_code == 200:

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    ticker = soup.select_one('#quote-header-info > div.Mt\(15px\) > div.D\(ib\).Mt\(-5px\).Mend\(20px\).Maw\(56\%\)--tab768.Maw\(52\%\).Ov\(h\).smartphone_Maw\(85\%\).smartphone_Mend\(0px\) > div.D\(ib\) > h1')
    ticker = ticker.get_text()
    ticker = ticker.split(')')[-2].split('(')[-1]
    # print(ticker)

    route = "ticker/1?"
    params = {'ticker': ticker}
    requestUrl = localhost + route + urllib.parse.urlencode(params)
    print(requestUrl)
    r = requests.post(requestUrl)
    print(r.text)

    # 4개월씩 3개
    i = 0
    start = 1
    end = 84
    for i in range(start, end):   #12월~9월(4개월)
        print(i)

        date = soup.select_one(
            '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td.Py\(10px\).Ta\(start\).Pend\(10px\) > span')
        if date is not None:
            print(date.get_text())
        else:
            print(date)

        open = soup.select_one(
            '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(2) > span')
        if open is not None:
            print(open.get_text())
        else:
            print(open)

        high = soup.select_one(
            '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(3) > span')
        if high is not None:
            print(high.get_text())
        else:
            print(high)

        low = soup.select_one(
            '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(4) > span')
        if low is not None:
            print(low.get_text())
        else:
            print(low)

        close = soup.select_one(
            '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(5) > span')
        if close is not None:
            print(close.get_text())
        else:
            print(close)

        volume = soup.select_one(
            '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(7) > span')
        if volume is not None:
            print(volume.get_text())
        else:
            print(volume)

        print("\n")

        mysqlDateForm = datetime.datetime.strptime(date.get_text(), '%b %d, %Y').strftime("%Y-%m-%d")
        print(mysqlDateForm)

        route = "daily/1?"
        params = {'ticker': ticker, 'date': mysqlDateForm, 'open': open.get_text(),
                  'high': high.get_text(), 'low': low.get_text(), 'close': close.get_text(),
                  'volume': volume.get_text().replace(",", "")}
        requestUrl = localhost + route + urllib.parse.urlencode(params)
        print(requestUrl)
        r = requests.post(requestUrl)
        print(r.text)

else:
    print(response.status_code)

    # wwww.mm.dd
    # String: date
    # double: 4
    # int: 1

SCROLL_PAUSE_SEC = 0.2

# selenium에서 사용할 웹 드라이버 절대 경로 정보
driverChrome = 'C:\\Users\\mrhi6-10\\Downloads\\chromedriver_win32\\chromedriver'
# selenium의 webdriver에 앞서 설지한 chromediriver를 연동
driver = webdriver.Chrome(driverChrome)

# driver로 특정 페이지를 크롤링
driver.get('https://finance.yahoo.com/quote/RIOT/history?period1=1577836800&period2=1609372800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true')

last_height = 0
new_height = 0

for i in range(1, 5):
    # 스크롤 높이에 3000만큼 더 가져옴
    new_height += 3000

    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo("+str(last_height)+", "+str(new_height)+");")

    time.sleep(SCROLL_PAUSE_SEC)



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

i = 0
while 1 :
    i = i + 1

    print(i)

    date = soup.select_one(
        '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td.Py\(10px\).Ta\(start\).Pend\(10px\) > span')
    if date is not None:
        print(date.get_text())
    else:
        print(date)
        break

    open = soup.select_one(
        '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(2) > span')
    if open is not None:
        print(open.get_text())
    else:
        print(open)
        break

    high = soup.select_one(
        '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(3) > span')
    if high is not None:
        print(high.get_text())
    else:
        break
        print(high)

    low = soup.select_one(
        '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(4) > span')
    if low is not None:
        print(low.get_text())
    else:
        print(low)
        break

    close = soup.select_one(
        '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(5) > span')
    if close is not None:
        print(close.get_text())
    else:
        print(close)
        break

    volume = soup.select_one(
        '#Col1-1-HistoricalDataTable-Proxy > section > div.Pb\(10px\).Ovx\(a\).W\(100\%\) > table > tbody > tr:nth-child('+ str(i) +') > td:nth-child(7) > span')
    if volume is not None:
        print(volume.get_text())
    else:
        print(volume)
        break

    print("\n")

print('end of loading')