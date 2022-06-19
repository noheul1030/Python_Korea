import pandas as pd
from openpyxl.workbook import Workbook      #xlsx(엑셀형태 파일)
import matplotlib.pyplot as plt


def 표만들기():
    번호 = [1,2,3]
    data = {
        '이름':['홍킬동','아무개','곽두팔'],
        '키':[175.5, 166.3, 180.0],
        '몸무게':[66.8, 50.7, 80.8]
    }

    df = pd.DataFrame(data, index = 번호)
    print(df)
    # 쓰기
    df.to_csv('myTable.txt', sep='\t')

    df.to_excel('myTable.xlsx', index=False)
    
    # 읽기
    df2 = pd.read_excel('myTable.xlsx')
    print(df2)

from matplotlib import font_manager, rc
# page 340
def 꺾은선():
    font_name = font_manager.FontProperties(fname='MALGUN.TTF').get_name()
    plt.rc('font', family=font_name)

    figure = plt.figure()
    axes = figure.add_subplot(111)          # 한개의 화면에 하나의 표 만들기
    x = ['1월','2월','3월','4월','5월','6월']           # 가로축
    y = [1200, 800, 500, 400, 700, 800]                 # 세로축
    
    axes.plot(x, y, linestyle = '-', marker = '^')
    plt.title('상반기 실적')
    plt.show()


def 원형그래프(data, y):
    font_name = font_manager.FontProperties(fname='MALGUN.TTF').get_name()
    plt.rc('font', family=font_name)
    
   
    plt.pie(data, autopct='%d%%')       # pie 데이터 넘김
    plt.legend(y)
    plt.title('비타민 함량')
    plt.show()          # 보여주기 


# 348 (1)
data = [0.18,0.3,3.33,3.75,0.38,25,0.25,2.75,0.1]      # 리스트 값
label = ['비타민A','비타민B1','비타민B2','나이아신','비타민B6','비타민C','비타민D','비타민E','엽산']      # 리스트 값

원형그래프(data, label)