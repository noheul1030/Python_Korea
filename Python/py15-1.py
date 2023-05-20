# page 78
'''
a = 15
print('{}>10:{}'.format(a,a>10))
print('{}<10:{}'.format(a,a<10))
print('{}>=10:{}'.format(a,a>=10))
print('{}<=10:{}'.format(a,a<=10))
print('{}==10:{}'.format(a,a==10))
print('{}!=10:{}'.format(a,a!=10))
'''
# page 79
# 0 : False(거짓)
# 0을 제외한 모든 숫자 : True(참)
'''
a = 10         # True (0을 제외한 모든 것은 True)
b = 0          # False

print('{}>0 and {}>0:{}'.format(a,b,a>0 and b>0))
print('{}>0 or {}>0:{}'.format(a,b,a>0 or b>0))
print('not{}:{}'.format(a,not a))
print('not{}:{}'.format(b,not b))

'''
a = 15
print(a>10)
print(a<10)
print(a>=10)
print(a<=10)
print(a==10)
print(a!=10)
