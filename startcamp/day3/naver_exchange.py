# 크롤링을 할 때 필요한 기능 모음(라이브러리) 가져오기
import requests # 요청을 보내고 응답을 받아오는 역할
from bs4 import BeautifulSoup   # 데이터를 구조화(예쁘게!)

url = 'https://finance.naver.com/marketindex/'

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(f'현재 원/달러 환율은 {exchange} 입니다.')