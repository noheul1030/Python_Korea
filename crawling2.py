import urllib.request
from bs4 import BeautifulSoup, Tag          # pip install bs4
url = urllib.request.urlopen('https://www.naver.com/')
html = url.read()
문자열 = html.decode()

# bs4로 자르기

soup = BeautifulSoup(문자열, 'html.parser')
tag = soup.find('title')
result= tag.text.strip()
print(result)
