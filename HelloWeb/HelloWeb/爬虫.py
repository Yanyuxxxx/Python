# import urllib.request
#
# url = "http://www.baidu.com"
# page_info = urllib.request.urlopen(url).read()
# page_info = page_info.decode('utf-8')
# print(page_info)



# from urllib import request
#
# url = 'http://www.baidu.com'
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# page = request.Request(url, headers = headers)
# page_info = request.urlopen(page).read().decode('utf-8')
# print(page_info)



from urllib import request
from bs4 import BeautifulSoup