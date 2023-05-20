'''
# 클래스 정의(설계)
class 자동차:
    def __init__(self, 차주인, 차종):
        self.name = 차주인
        self.car = 차종
    def 차정보(self):
        print('{}차의 주인은 {}입니다.'.format(self.car,self.name))
    def 차변경(self, 차종):
        self.car = 차종
    def __del__(self):
        print('{}차 안내 종료'.format(self.name))

# 클래스 사용
# 객체화(클래스 사용을 위해 변수로 만들어줌)
아빠차 = 자동차('아빠','벤츠')         # 클래스 사용 1
엄마차 = 자동차('엄마','아반떼')       # 클래스 사용 2
내차 = 자동차 ('내','아우디')           # 클래스 사용 3

아빠차.차정보()
엄마차.차정보()
내차.차정보()
del 아빠차          # 아빠차 변수를 강제로 없앰
엄마차.차변경('제네시스')
엄마차.차정보()
# 아빠차.차정보()---삭제됨      # 아빠차 변수가 이미 없어졌으므로 사용 불가

'''
# page 287 문제 (1번)

population = 0

class Person:
    def __init__(self,name):
        global population       # 클래스보다 위에 있는 전역변수를 수정할 때
        population +=1
        print('{} is born'.format(name))
        self.name = name
       
    def get_population(self):
        return population

    def __del__(self):
        global population       # 클래스보다 위에 있는 전역변수를 수정할 때
        population -= 1
        print('{} is dead'.format(self.name))
                
man = Person('제임스')
woman = Person('에밀리')

print('전체 인구수: {} 명'.format(population))

del man

print('전체 인구수: {} 명'.format(population))
input('종료')