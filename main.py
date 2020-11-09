from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

def PrintPageContent(specialty):
    resp = urlopen("https://vuzoteka.ru/%D0%B2%D1%83%D0%B7%D1%8B/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/{0}".format(quote(specialty)))
    sp = BeautifulSoup(resp)

    #links = sp.find_all('a', class_="institute-search-title h3")
    name = sp.find_all('h1')
    #points = sp.find_all('div', class_="label-value")

    univers = sp.find_all('div', class_="institute-row")
    
    for i in range(len(name)):
        print(str(name[i])[str(name[i]).index('>')+1:str(name[i]).rindex('<')])

    print('')

    uninfo = []

    for i in range(len(univers)):
        uninfo.append('')
        #print(str(links[i])[str(links[i]).index('>')+1:str(links[i]).rindex('<')], end=' ')
        uninfo[i]+= univers[i].text[0:univers[i].text.index('студентов')]+"\n"
        uninfo[i]+= univers[i].text[univers[i].text.index('студентов'):univers[i].text.index('студентов')+9]+" "
        uninfo[i]+= univers[i].text[univers[i].text.index('студентов')+9:univers[i].text.index('город')]+"\n"
        uninfo[i]+= univers[i].text[univers[i].text.index('город'):univers[i].text.index('средн')]+"\n"
        uninfo[i]+= univers[i].text[univers[i].text.index('средн'):univers[i].text.index('средн')+10]+" "
        uninfo[i]+= univers[i].text[univers[i].text.index('средн')+10:univers[i].text.index('ранг')]+"\n"
        uninfo[i]+= univers[i].text[univers[i].text.index('егэ', univers[i].text.index('ранг'), -1):univers[i].text.index('места')]+"\n"
        uninfo[i]+= univers[i].text[univers[i].text.index('места'):univers[i].text.index('баллы')]+"\n"
        uninfo[i]+= univers[i].text[univers[i].text.index('баллы'):univers[i].text.index('стоимость')]+"\n"
        uninfo[i]+= univers[i].text[univers[i].text.index('стоимость'):univers[i].text.index('обучение')]+"\n"
        uninfo[i]+= univers[i].text[univers[i].text.index('обучение'):-10]+"\n"
        uninfo[i]+= univers[i].text[-10:-1]+"\n"
        print(uninfo[i])
        #print(str(points[i])[str(points[i]).index('</span>')+7:str(points[i]).rindex('<span')])
        print('')
        print('')

print("Укажите полное название специальности. Например:Фундаментальная информатика и информационные технологии 02 03 02")
spec = input('>>> ').replace(" ", "-").replace(".", "-")

PrintPageContent(spec)
