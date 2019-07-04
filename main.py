import requests
from bs4 import BeautifulSoup


# Caso não apareça nenhum resultado, abrir esse link no navegador manualmente e depois rodar o programa
source = 'https://www.guichevirtual.com.br/campo-mourao-pr-v-farol-pr?ida=2019-07-09'

r = requests.get(source)
print(r.headers)

soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.prettify())

precos  = soup.findAll(class_="passagens-comprar-preco")
print(type(precos))
resultados = list()
for p in precos:
    #print(p)
    l = (p.text.split('R$ '))
    print((l[1].strip().replace(',','.')))
    resultados.append((l[1].strip().replace(',','.')))

print('\nDisplay all headers\n')