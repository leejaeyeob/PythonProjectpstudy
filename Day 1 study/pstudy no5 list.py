'''
List
    단일 변수에 여러 항목을 저장하는데 사용된다.
    List 항목은 순서가 지정되고 변경 가능하며 중복값 허용
    List 에는 다양한 데이터 유형이 포함될 수 있다.
'''
thislist = ["팔찌", "반지", "목걸이"]
print(thislist[2])

# List 길이
print(len(thislist))

# List 데이터 유형
list1 = ["팔찌", "반지", "목걸이"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, False]

# 다양한 유형 포함가능
list4 = ["abc", 40, False, 343]

# 항목 접근
thislist = ["팔찌", "반지", "목걸이"]
print(thislist[2])

# 변경
thislist[1] = "다이아몬드"
print(thislist)

# 항목 변경 2개
thislist = ["팔찌", "반지", "목걸이", "귀걸이", "모자", "신발"]
thislist[1:3] = ["발찌", "시계"]
print(thislist)

# 두번째 세번째 값을 하나의 값으로 변경
thislist = ["팔찌", "반지", "목걸이", "귀걸이", "모자", "신발"]
thislist[1:3] = ["시계"]
print(thislist)

# 항목 추가
thislist = ["팔찌", "반지", "목걸이"]
thislist.append("시계")
print(thislist)

# 항목 추가 - 인덱스 번호로 추가
thislist = ["팔찌", "반지", "목걸이"]
thislist.insert(1, "시계")
print(thislist)

# 항목 값으로 제거
thislist = ["팔찌", "반지", "목걸이"]
thislist.remove("팔찌")
print(thislist)

# 항목을 지정된 인덱스로 제거
thislist = ["팔찌", "반지", "목걸이"]
thislist.pop(2)
print(thislist)

# 마지막 값 제거
thislist = ["팔찌", "반지", "목걸이"]
thislist.pop()
print(thislist)

# 목록 삭제
thislist = ["팔찌", "반지", "목걸이"]
thislist.clear()
print(thislist)

# 확장
thislist = ["팔찌", "반지", "목걸이"]
thislist.extend(["시계", "모자"])
print(thislist)

# 객체 삭제
# del thislist
# print(thislist)


