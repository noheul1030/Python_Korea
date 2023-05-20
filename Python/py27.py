# # page 136~140

# # (1) 수도 맞추기
# while True :
#     city = input('대한민국의 수도는 어디인가요?>>> ')
#     if city =='서울' or city == 'seoul' or city == 'SEOUL' :
#         print('정답입니다.')
#         break
#     else :
#         print('오답입니다. 다시 시도하세요.')

# # (2) 취미 입력하기
# hobbies = []
# while True :
#     hobby = input('취미를 입력하세요(종료는 그냥 엔터)>> ')
#     if hobby =='' :
#         print('입력된 취미가 모두 저장되었습니다.')
#         break
#     else :
#         hobbies.append(hobby)
#     print(hobbies)

# # (3) 과일 입력하기
# fruits = ['사과','감귤']
# count = 3

# while count > 0 :
#     fruit = input('어떤 과일을 저장할까요?>>> ')
#     if fruit in fruits :
#         print('동일한 과일이 있습니다.')
#         continue
#     fruits.append(fruit)
#     count -= 1
#     print('입력이 {}번 남았습니다.'.format(count))
# print('5개 과일은 {}입니다.'.format(fruits))

# # (4) 합 구하기
# count = 0
# total = 0
# while count < 5 :
#     n = int(input('{}번쨰 정수를 입력하세요>>> '.format(count + 1)))
#     if n <= 0 :
#         print('0이하의 정수는 처리할 수 없습니다.')
#         continue
#     total += n
#     count += 1
# print('입력된 5개 양수의 총 합은 {}입니다.'.format(total))

# # page 141 (1)
돈 = 10000
잔액 = 0
while 잔액 < 돈 :
    사용 = int(input('사용할 금액 입력>>> '))
                
    if 돈 < 사용:
        print('{}원이 부족합니다.'.format(사용-돈))
        print('현재 {}원이 있습니다.'.format(돈))
        continue
    elif 사용 <= 0 :
        print('0이하의 금액은 사용할 수 없습니다.')
        continue

    돈 -= 사용
    
    print('현재 {}원이 있습니다.'.format(돈))
    if 돈 == 0 :
        break
