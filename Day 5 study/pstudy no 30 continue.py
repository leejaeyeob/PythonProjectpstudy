'''
continue
    while문이나 for문과 같은
    반복문을 강제로 건너뛰기
    (아래 코드 실행하지 않는다)
'''
total = 0
for a in range(1, 101):
    if a % 3 == 0:
        continue
    total += a
    print('a: {}, total {}'.format(a, total))

print(total)
