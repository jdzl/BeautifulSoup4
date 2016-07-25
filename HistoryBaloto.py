from bs4    import BeautifulSoup
from urllib import urlopen

class Baloto (object):
    def __init__(self,b,fecha):
        self.b = b      
        self.fecha = fecha

        
web = urlopen('http://www.baloto.com/filtro-historico-de-resultados.php').read()
html = BeautifulSoup(web,"html.parser")

historico_baloto = list()

table = html.findAll('table')
tr = table[0].findAll('tr')

for i in range(3,len(tr)):
    td = tr[i].findAll('td')
    if(len(td)>4):
        bolas,fecha = td[1].text.split(' - '),td[5].text    
        baloto = Baloto(bolas,fecha)
    
    historico_baloto.append(baloto)

print "Fecha       Baloto "
for i in range(0,len(historico_baloto)):
    print historico_baloto[i].fecha, "-".join( historico_baloto[i].b ) 
    
