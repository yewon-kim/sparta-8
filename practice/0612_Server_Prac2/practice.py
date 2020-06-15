import re

comment_receive = "https://www.naver.com https://www.google.com https://www.daum.net"

regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

def regex_search_group(string, regex):
    pattern = re.compile(regex)
    m = pattern.search(string)
    if m : return m.group()
    else: return None