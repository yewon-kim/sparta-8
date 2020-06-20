import re

def regex_search_group(string, regex):
    pattern = re.compile(regex)
    m = pattern.search(string)
    if m : return m.group()
    else: return None

regex_url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

comment_receive = "다음 링크들을 확인해 보세요. https://www.naver.com https://www.google.com https://www.daum.net"

url_receive = regex_search_group(comment_receive, regex_url)

print(url_receive)