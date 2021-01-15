menu = ['예향정', '착한통큰오리삼겹', '장가계', '첨단공원국밥']
#print(menu)
#print(menu[0], menu[-1])

phone_book = {'예향정': '123-123', '첨단공원국밥': '456-456', '장가계': '789-789'}
# print(phone_book)
# print(phone_book['첨단공원국밥'])

# 1. 가게 하나 랜덤으로 추천받기
import random
#print(phone_book[random.choice(menu)])
my_menu = random.choice(menu)
print(my_menu + '의 전화번호는' + phone_book[my_menu] + '입니다.')

#f-string -> python 3.6 변수들을 문자열에 넣을 수 있다.
print(f'{my_menu}의 전화번호는 {phone_book[my_menu]} 입니다.')

