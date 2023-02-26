'''
r (read mode) : 읽기 전용 모드 / 파일 없으면 에러

경로
    절대경로 예) C://Users//PythonProject//Day 7 study//hello.txt
    상대경로 예) /hello.txt
                ../../resourses /hello.txt
            . -> 현재폴더
            .. -> 상위폴더
    최상위 경로(root) / 또는 C:/ (윈도우 OS)
'''
file = open('hello.txt', 'rt', encoding='UTF=8')
str = file.read()
print(str, end='')
file.close()

print()

with open('hello.txt', 'rt', encoding='UTF=8') as file:
    str = file.read()
    print(str, end='')