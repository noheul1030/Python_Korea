# 예제1
if True:
    print('맞습니다.')
if False:
    print('틀립니다.')
if 22 > 21 :
    print('22가 21보다 큰가?')

# 예제2 
age = int(input('당신의 나이는 몇살입니까? >>> '))
if age >= 20 :
    print('당신은 성인입니다.')
elif age < 20 and age > 13 :
    print('당신은 청소년 입니다.')
elif age > 0 and age <= 13 :
    print('당신은 어린이 입니다.')
else :
    print('?')

# 예제3
체온 = float(input('온도를 입력해주세요 : '))
if 체온 < 35.0 :
    print('저체온증!!!')
elif 체온 <= 37.5 :
    print('정상 체온입니다.')
elif 체온 < 45.0 :
    print('체온이 높습니다!!!')
else :
    print('?')
