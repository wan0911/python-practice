import urllib.request as req
from bs4 import BeautifulSoup

f = open('./알라딘중고샵.txt', 'w')
page_num = 1
while True:
    code = req.urlopen('https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyLastWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}'.format(page_num))
    soup = BeautifulSoup(code, 'html.parser')
    title = soup.select('a.bo3 > b')
    price = soup.select('a.bo_used > b')
    if len(title) == 0:
        break

    for i in range(len(title)):
        print(title[i].string, price[i].string)
        f.write(title[i].string + "," +  price[i].string)
    page_num += 1

f.close()


'''
알라딘 top 100 title -> txt로 출력
'''
