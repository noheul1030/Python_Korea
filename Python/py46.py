import csv          # import : 파일 복붙

경로 = 'C:\\Users\\Administrator\\Desktop\\내파일.csv'

# 함수 정의
def 엑셀쓰기():
    f = open(경로,'w',newline = '')     # w :새로쓰기
    내용 = csv.writer(f)         # 메모장 들어갈 내용
    내용.writerow(['일','이','삼'])
    f.close()

def 엑셀추가쓰기():
    f = open(경로,'a',newline = '')     # a :추가쓰기
    내용 = csv.writer(f)         # 메모장 들어갈 내용
    내용.writerow(['사','오','육'])
    f.close()

def 엑셀읽기():
    f = open(경로,'r',newline = '')     # r :내용 읽기
    내용 = csv.reader(f)        # 엑셀내용 전부 읽어옴

    for row in 내용 :
        for col in row :
            print(col, end ='\t')
        print()
    
    f.close()


# 함수 사용
