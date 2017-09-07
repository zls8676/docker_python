import  urllib.request
from bs4 import BeautifulSoup

def youku():
    url = "http://www.youku.com"
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    # print(html)
    soup = BeautifulSoup(html,"html.parser")
    a = soup.findAll('a')
    b = set()
    for i in a:
        b.add(i['href'])

    # for c in b:
    #     print(c)


    return b



yk = youku()
for i in yk:
    # b = str(i)

    with open("yk.txt","a+")  as f:
            # b = i.read()
        f.write(i)
