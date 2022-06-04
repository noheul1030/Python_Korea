# page 99 (1)
score = int(input('writing the score >>> '))

if score <=100  and score >=90 :
     학점=('A학점') 
elif score >=80 :
     학점=('B학점') 
elif score >=70 : 
     학점=('C학점') 
elif score >=60 :
     학점=('D학점') 
else :
     학점=('F학점')

print('점수는 {} 점이고,학점은 {} 입니다.'.format(score,학점))

# page 99 (2)
a = int(input('writing the number >>> '))

if (a%3) == 0 :
     print( a,'is 3배수이다.')
else :
     print( a,'is 3배수 아니다.')
     
# page 99 (3)
#while True:
a = int(input('1.number >>> '))
b = int(input('2.number >>> '))
c = int(input('3.number >>> '))
d = ()

if a > b and a > c :
     d =a
elif b > a and b > c :
     d = b
elif c > a and c > b :
     d = c
print()
print('Big number is {}.'.format(d))

#page 99 (4)

차량번호 = input('차량번호를 입력하세요 >>> ')

numbers = int(차량번호[-1:])

print()
if (numbers%2) == 0 :
     print('차량번호 {}는 오늘 운행가능 입니다.'.format(차량번호))
else :
     print('차량번호 {}는 오늘 운행불가 입니다.'.format(차량번호))