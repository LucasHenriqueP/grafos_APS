# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import networkx as nx
import matplotlib.pyplot as plt

'''Carrega o Arquivo Json'''
arq = open('entradas.json')
cidades = json.load(arq)

'''Cria um Grafo Vazio'''
G = nx.Graph()
print("\n\n---------------------- Começo do Parsing ---------------\n")

'''Trecho que faz os Parsing e Scraping'''
for i in cidades['cidades']:

    print("Origem: "+i['origem']+"")

    '''Adiciona uma cidade Origem'''
    G.add_node(i['origem'])

    print("Destino: "+i['destino']+"")

    '''Adiciona uma cidade Destino'''
    G.add_node(i['destino'])

    print(i['link'])
    source = i['link']

    '''Faz um Request no Link do site paga Obter as informações'''
    r = requests.get(source)
    soup = BeautifulSoup(r.content, 'html.parser')
    precos  = soup.findAll(class_="price-value")
    resultados = list()
    for p in precos:
        l = (p.text.split('R$'))
        resultados.append(float((l[1].strip().replace(',','.'))))
    print("Preco: "+str(min(resultados))+"\n\n")

    '''Adiciona uma Aresta entre os Vertices de Origem e Destino'''
    G.add_edge(i['origem'],i['destino'],weight=min(resultados))


print("\n\n---------------------- Fim do Parsing ---------------\n")

print("Caminho mais Curto entre duas Cidades: ")
path =list(nx.shortest_simple_paths(G, source="Ivailandia", target="Campo Mourao"))
print(path[0])

T = nx.minimum_spanning_tree(G)

print("\nGrafo Gerada: ")
print(list(G.edges(data=True)))

print("\nMST Gerada: ")
print(list(T.edges(data=True)))

subG= nx.Graph()


for n in path[0]:
    subG.add_node(n)

for i in range(len(path) -2):
    subG.add_edge(path[0][i], path[0][i+1])   

plt.subplot(221)
nx.draw(G, with_labels=True, font_weight='bold')

plt.subplot(222)
nx.draw(T, with_labels=True, font_weight='bold')

plt.subplot(223)
nx.draw(subG, with_labels=True, font_weight='bold')

plt.show()
