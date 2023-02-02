'''
set
    순서가 없다
    인덱싱되지 않는 컬렉션
    중복값 없다.
'''
thisset = {"현대", "기아", "대우"}
# 실행할 때마다 순서가 변경
print(thisset)
# 항목 가져오기
for x in thisset: #thisset 길이 만큼 반복
    print(x)

# 값이 있는지 확인
thisset = {"현대", "기아", "대우"}
print("현대" in thisset)
print("폭스바겐" in thisset)

# 항목 추가하기
thisset.add("혼다")
print(thisset)

# 다른 set 항목 추가
thisset1 = {"현대", "기아", "대우"}
thisset2 = {"혼다", "마쯔다", "미쯔비시"}
thisset1.update(thisset2)
print(thisset1)

# 항목 제거
thisset = {"현대", "기아", "대우"}
thisset.remove("대우")
print(thisset)

thisset = {"현대", "기아", "대우"}
thisset.discard("현대")
print(thisset)

# 항목제거
thisset.pop()
print(thisset)

# 비우기
thisset.clear()
print(thisset)

