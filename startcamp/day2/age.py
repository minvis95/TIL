import requests

# API 요청 URL 확인 + 필요한 데이터 건네주기
name = 'chanwoo'
# name = input()
url = f'https://api.agify.io/?name={name}'

# URL로 요청 보내기
response = requests.get(url).json() #url을 분석해서 json으로 바꿔준다.
print(type(response))
# print(response)
# 응답 결과 확인 후 
name = response['name']
age = response['age']

print(f'{name}님의 예상 나이는 {age}살 입니다.')

# 복습 nationalize.io
# API라는 수단을 활용하여 의사소통한다.