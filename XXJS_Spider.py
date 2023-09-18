#_*_encoding='utf-8'_*_
import urllib.request
import re
import requests
response=urllib.request.urlopen('http://10.209.85.202/xxjs/')
a=str(response.read().decode('utf-8'))
result=re.findall('<li.*?href="(.*?)".*?</a>',a,re.S)
result=result[2:]
for i in result:
    b=re.search('.*/(.*)',i).group(1)
    response=requests.get('http://10.209.85.202/xxjs/'+i)
    with open (b,'wb') as f:
        f.write(response.content)
    print('正在下载',b)
