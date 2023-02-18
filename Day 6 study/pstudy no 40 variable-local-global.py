'''
지역변수(local)
    함수 내부 선언
    함수 내부에서만 사용가능

전역변수(global)
    함수 외부선언
    함수 내부 외부 모두 사용가능
'''

gVar = '전역'
def globalAndLocal():
    lVar = '지역'
    print(gVar, '변수입니다') # 전역변수 참조만 하고 있다
    print(lVar, '변수입니다.')

globalAndLocal()
print(gVar)
# print(lVar) 지역 변수라 오류발생

# 전역변수 선언
total = 0
def gift(dic, who, money):
    global total # 전역변수 total 사용
    total += money
    dic[who] = money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 6)
gift(wedding, '이모', 10)
print('축의금 명단 : {}'.format(wedding))
print('전체 축의금: {}'.format(total))