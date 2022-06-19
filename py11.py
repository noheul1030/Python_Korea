var1 = int(input('입력하세요1:'))
var2 = int(input('입력하세요2:'))
# input의 값은 문자열(글자)로 나온다
print(var1 - var2)

var3 = float(input('파이값은 얼마일까요?'))
print(var3)

# int : 숫자 (소수점없는 숫자, 정수)
# float : 숫자 (소수점있는 숫자, 실수)
# str : 글자(문자열)

# page 65, page 66(1)
price = 50000
n = int(input('할부 개월 입력 >>'))
print('매달 내는 돈은 {}원 입니다.'.format(price/n))

# page 66(1)
'''
첫 번째 실수를 입력하세요 >>> 1.23
두 번째 실수를 입력하세요 >>>2.34
1.23와 2.34의 합은 3.57입니다.
'''
