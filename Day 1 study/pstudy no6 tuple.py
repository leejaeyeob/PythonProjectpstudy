'''
튜플
    단일 변수에 여러 항목을 저장하는데 사용된다.
    순서가 있고, 변경할 수 없는 List
    둥근 괄호로 작성된다.
'''
thistuple = ("젠쿱", "투스카니", "티뷰론")
print(thistuple)
# 튜플 길이
print(len(thistuple))

# 항목 접근
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

# 튜플값 변경 방법
thistuple = ("젠쿱", "투스카니", "티뷰론")
thiscast = list(thistuple) # casting / 형변환
thiscast[1] = "포르쉐"
thistuple = tuple(thiscast)
print(thistuple)

# 튜플 압축 풀기
thistuple = ("젠쿱", "투스카니", "티뷰론", "포르쉐")
(p1, p2, p3, p4) = thistuple
print(type(p1))
print(p2)
print(p3)
print(p4)

# 두개의 튜플 조인
thistuple1 = ("젠쿱", "투스카니", "티뷰론", "포르쉐")
thistuple2 = ("현대", "기아", "쌍용", "대우")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)