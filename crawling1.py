# 크롤링 : 웹페이지에서 원하는 문자를 가져오는 기술
import urllib.request

# 가져올 페이지의 주소(URL)을 써줍니다.
url = urllib.request.urlopen('https://www.daum.net/')

# 해당 웹페이지의 웹코드를 읽는다
html = url.read()
# 웹코드(html)를 파이썬 문자열로 바꾼다
문자열 = html.decode()

# 출력
print(문자열)
