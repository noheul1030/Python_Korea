# 리스트 = []
# 세트 = set({})
# 튜플 = ()

# 리스트.append(1)
# 리스트.append(2)
# 리스트.append(2)
# print(리스트)

# # set 추가하기(중복불가)
# 세트.add(1)
# 세트.add(2)
# 세트.add(2)
# # set 제거하기
# 세트.discard(2)
# print(세트)

# 튜플 = tuple(리스트)
# print(튜플)

# page 67 (4)

n = 1
여행리스트 = set({})
while n < 4 :
    
    수학여행지 =input('희망하는 수학여행지를 입력하세요>>> ')
    
    여행리스트.add(수학여행지)
    n += 1
print('조사된 수학여행지는', 여행리스트,'입니다.')


