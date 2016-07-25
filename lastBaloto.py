from bs4    import BeautifulSoup
from urllib import urlopen

url = 'http://www.baloto.com/#node4de5.html?qt-navegacion_internas_baloto=2#qt-navegacion_internas_baloto'
web = urlopen(url).read()
soup = BeautifulSoup(web,"html.parser")


div= soup.findAll('div',
                  attrs={'class': "content"}
                  )

span= div[0].findAll('span')
print "Ultimo juego Baloto"
for i in range(4,10):    
    print span[i].text,

