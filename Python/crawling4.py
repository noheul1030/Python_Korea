import urllib.request
from bs4 import BeautifulSoup        # pip install bs4

# 1. url 설정
url = urllib.request.urlopen('https://movie.naver.com/movie/bi/mi/basic.naver?code=154285#')
html = url.read()
문자열 = html.decode()

리스트 = []
soup = BeautifulSoup(문자열, "html.parser")
# 2. 규칙성이 있는 최소단위로 모두 추출
tag = soup.find_all("div", class_="tx_top")
for i in tag :
    # 3. <>를 기준으로 자르고 <>를 없앤다.
    result= i.find("strong").text.strip()
    # 태그 없애기
    # result = i.text.strip()
    리스트.append(result)

print(result)

for j in 리스트 :
    print(j)
print('내가 볼 영화는>> ',리스트[0])