# for 변수명 in range(10):

#while
# import time

# 기준점 = 0
# while 기준점<10:        ----------> 10번 출력
#     time.sleep(1)      
#     print('10은 5보다 큽니다.')
#     기준점 += 1 
# print('프로그램 종료')
'''
while 조건 :
    조건이 맞을때마다 실행할 코드
'''
# num = 1
# while num < 11 :
#     print(num,'번 했습니다.')
#     num += 1 

# # page 105

# n = 10
# while n >= 1 :
#     print(n,'번 했습니다.')
#     n -= 1    

# page 111 (1)

'''
숫자 1개를 입력받고
그 숫자만큼 hello 하기
단, 0 이하의 숫자를 입력할 경우
'잘못된 숫자'입니다만 해주기
'''
기준= 0
입력값= int(input('정수를 입력하세요 >>> '))

while 기준 < 입력값 :
    print(기준+1,'번째 hello')
    기준 += 1
if 입력값 <= 0 :
    print('잘못된 숫자입니다.')

# page 111 (2)

'''
0~100까지 숫자 중에서
7의 배수만 출력하기
(반복문 사용)
'''
for number in range(1,100):
    if number%7 == 0 :
        print(number)
'''
flag= 1
while flag < 101:
    if flag % 7 == 0 
        print(flag)
    flag = flag + 1         # flag += 1

'''
# page 110

dan = 2
while dan <= 9 :
    n = 1
    while n <= 9 :
        print('{}*{}={}'.format(dan,n,dan*n))
        n += 1
        dan += 1        

