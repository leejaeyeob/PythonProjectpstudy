'''
내장 데이터 유형
python 변수는 다른 유형의 데이터를 저장할 수 있으며
다른 유형은 다른 작업을 수행할 수 있다.

텍스트 유형 : str
숫자 유형 : int, float, complex
스퀸스 유형 : list, tuple, range
매핑 유형 : dict
세트 유형 : set
부울(논리) 유형 : bool
바이너리 유형 : bytes, bytearray
없음 유형 : NoneType
'''
# str
x = "hello world"
print(type(x))
# int
x = 20
print(type(x))
# complex
x = 1j
print(type(x))

# list
x = ("반지", "팔찌", "목걸이")
print(type(x))
# tuple
x = ("반지", "팔찌", "목걸이")
print(type(x))
# range
x = ("반지", "팔찌", "목걸이")
print(type(x))
# range
x = range(6)
print(type(6))
# dict
x = {"name":"이재엽", "기술":"드리프트"}
print(type(x))
# set
x = {"반지", "팔찌", "목걸이"}
print(type(x))
# bool(논리)
x = True #false
print(type(x))

# 숫자 + 숫자 = 숫자
# 문자 + 숫자 = 문자숫자
num1 = 10
num2 = 20
result = num1 + num2
print(result)
name = '양선용'
age = '21'
자기소개 = '차쟁이'
result = name + '/' + age + '/' + 자기소개
print(result)
