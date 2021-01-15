import requests, pprint

name = 'ruby'

# ?로 나뉘어진다. 뒤는 추가데이터 
# 쿼리스트링 = ?name = micael
url = f'https://api.nationalize.io/?name={name}'

# .text() 와 .json() 괄호는 메서드(어떠한 기능)을 실행 -> 강제로 만들어 낸다.
# 괄호가 없으면 애가 가지고 있는 text 데이터를 꺼낸다.
response = requests.get(url).json()
# pprint.pprint(response)
# print(type(response)) # json안쓰면 그냥 str이였어.. 그래서 .json 써서 json화 해서 강제로 만들어
name = response['name']
country_id = response['country'][0]['country_id']
probability = round(response['country'][0]['probability'] * 100, 2)

print(f'{name}의 국적은 {probability}% 확률로 {country_id}입니다.')

# 무조건 참고자료는 python docs로!!
# national이라는 api를 활용하는것