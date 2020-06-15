import requests
from bs4 import BeautifulSoup

url = 'https://www.donga.com/news/Inter/article/all/20200614/101501448/1'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')
og_site = soup.select_one('title')

url_image = og_image['content']
url_title = og_title['content']
url_description = og_description['content']
url_site = og_site.text

print(url)
print(url_image)
print(url_title)
print(url_description)
print(url_site)