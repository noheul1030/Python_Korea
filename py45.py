경로 = 'C:\\Users\\Administrator\\Desktop\\텍스트.txt'

# 함수 정의
def 메모장쓰기(text):
    f = open(경로,'w',encoding='UTF-8')
    f.write(text)         # 메모장 들어갈 내용
    f.close()

def 메모장추가쓰기(text):
    f = open(경로,'a',encoding='UTF-8')
    f.write(text)         # 메모장 들어갈 내용
    f.close()

# def 메모장연속쓰기():
#     while True :
#         myText = input('입력할 문자 (0입력하면 탈출)>>> ')
#         if myText == "0" :
#             break
#         else :
#             메모장추가쓰기('\n'+myText)

def 메모장읽기():
    f = open(경로,'r',encoding='UTF-8')
    lines = f.readlines()
    for line in lines:
        print(line, end='')
    f.close()


# 함수 사용
