from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://vuzoteka.ru/%D0%B2%D1%83%D0%B7%D1%8B/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0-%D0%B8-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B5-%D0%BD%D0%B0%D1%83%D0%BA%D0%B8-02-03-01')
sp = BeautifulSoup(resp)

links = sp.find_all('a', class_="institute-search-title h3")
name = sp.find_all('h1')
points = sp.find_all('div', class_="label-value")

for i in range(len(name)):
    print(str(name[i])[str(name[i]).index('>')+1:str(name[i]).rindex('<')])

print('')

for i in range(len(links)):
    print(str(links[i])[str(links[i]).index('>')+1:str(links[i]).rindex('<')], end=' ')
    print(str(points[i])[str(points[i]).index('<span class="inner-a0 mark-label-c0 color-b0">Б</span>')+55:str(points[i]).rindex('<span class="inner-a0 margin-l0 mark-label-c0 color-b1">Д</span>')])

