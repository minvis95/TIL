# 공공 데이터 API 활용 실습(대기오염정보)

# 1. 필요한 라이브러리 import 하기
import requests, pprint

# 2. API URL 및 KEY 값 확인
key = 'rFJC3cDlduX33VevCCiVLHZzxbbXCkSZoZYA3ckCSM%2BGnPd%2BNnGm4tN96td9rxJuAUneJ8yAPf79bdlFPxHvzg%3D%3D'
sidoName = '서울'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={sidoName}&returnType=json'

# 3. 요청 및 응답값 확인
response = requests.get(url).json()

# pprint.pprint(response)

sido_name = response['response']['body']['items'][0]['sidoName']
pm_10 = response['response']['body']['items'][0]['pm10Value']
station_name = response['response']['body']['items'][0]['stationName']

# 4. 최종 출력 문자열
text = f'{sido_name}의 미세먼지 농도는 {pm_10}입니다. (측정소:{station_name})'

#5. 텔레그램 메시지 전송(sndMessage)
token = ''
chat_id = ''
api_url = f'https://api.telegram.org/bot{token}'

telegram_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(telegram_url) 