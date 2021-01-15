# 가장 최근에 메시지를 보낸 사용자에게,
# '안녕하세요' 메시지 보내기.

# 1. 요청에 필요한 라이브러리를 Import
import requests, pprint

# 2. API 요청 URL + Token 확인
token = ''
api_url = f'https://api.telegram.org/bot{token}'

# 3. 메시지 보낸 사용자의 ID값 찾기
chat_id_url = f'{api_url}/getUpdates'
response = requests.get(chat_id_url).json()
# pprint.pprint(response)

chat_id = response['result'][0]['message']['chat']['id']
# print(chat_id)

# 4. chat_id 에게 메시지 보내기
text = input('메시지를 입력하세요:')
message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)   # 메시지만 보낼꺼니깐