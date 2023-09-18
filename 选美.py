import requests
import os
import random
#from PIL import Image
from io import BytesIO
headers={'X-CSRFToken': '4jd8oHVCpl1BiFs2D6945mrBtZlejhy0AtLyizju590iTFLbARlabCyhb8zC37aI',
             'Cookie':'_ga=GA1.1.1063559671.1668824904; _gid=GA1.1.1656275950.1681978312; csrftoken=4jd8oHVCpl1BiFs2D6945mrBtZlejhy0AtLyizju590iTFLbARlabCyhb8zC37aI; sessionid=gztl7thwnv4th7v1z66r12q2bgvuwr6c',
             'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.95'}
acc=['d53ce405e0080bed7e324dd76f3e687b','f50d337717354fd60e6fca36cd2e4d83','ff9fb07e181acce4b358cb2e096a1f29']
BASIC_URL='http://114.55.172.240:180/api/submission?id='
data=[]
for i in range(3):
    s=requests.get('http://114.55.172.240:180/api/submission?id='+acc[i],headers=headers).json()['data']['code']
    data.append(s.split(' '))
def get_img(idm):
    url = 'http://10.209.85.202/score/photo/' + idm + '.jpg'
    response = requests.get(url)
    return response.content
def chosen():
    chose=random.randint(0,768)
    while int(data[0][chose][-2])%2==1:
        chose=random.randint(0,768)
    avi=[data[0][chose],data[1][chose],data[2][chose]]
    return avi
for i in range(100):
    d=chosen()
    with open(d[0]+'.jpg','wb') as f:
        f.write(get_img(d[0]))
'''for i in range(3):
    image = Image.open(BytesIO(get_img(d[0])))
    image.show()'''