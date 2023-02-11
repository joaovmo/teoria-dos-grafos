import networkx as nx
import matplotlib.pyplot as plt

def exibir_grafo(G):
  plt.figure(2)
  nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
  plt.show()
#cria grafo vazio
G = nx.Graph()


# Instanciando o objeto Grafo 2
G1 = nx.Graph()

G1.add_nodes_from(["V1","V2","V3","V4","V5"])
G1.add_edges_from([("V1","V2"),("V1","V3"),("V3","V4"),("V4","V5"),("V5","V2")])











#adiciona vertices
G.add_node('v1')
G.add_node('v2')
G.add_node('v3')
G.add_node('v4')
G.add_node('v5')

#adiciona arestas
G.add_edge('v1', 'v2')
G.add_edge('v2', 'v3')
G.add_edge('v3', 'v4')
G.add_edge('v4', 'v5')
G.add_edge('v5', 'v1')
G.add_edge('v2', 'v4')

#lista vertices
print('lista de vertices')
print(list(G.nodes()))
input()

#percorre o conjunto de vertices
print('Percorrendo os vértices')
for v in (list(G.nodes())):
    print(v)
input()

#Lista de arestas 
print('lista de aresta')
print(list(G.edges()))
input()


#percorre o conjunto de arestas
print('Percorrendo as aresta')
for e in (list(G.edges())):
    print(e)
input()


#mostra a lista de graus (grau é a quantidade de vertice {bolinhas} que ele esta ligado)
print('Lista de graus de G')
print(list(G.degree()))
input()

#percorrendo os graus:
print('Percorrendo os graus de G com for')
for gra in (list(G.degree())):
    print(gra)
input()

#mostra o grau especifico
print('grau do v2')
print(G.degree()['v2'])
input()


#mostra o grau de v2 usando funçao
def grau_vertice(grafo, v):
    lista1 = list(grafo.neighbors(v))
    return len(lista1)


print('grau do v2 usando def')
print(grau_vertice(G, 'v2'))


#percorre a vizinhanca de v1 com o for
print('Percorrendo a vizinhança de v1 com for')
for ga in (list(G.neighbors('v1'))):
    print(ga)
input()



for vertice in list(G.nodes):
    grau_do_vertice = grau_vertice(G, vertice)

    print("Grau do vértice %s: %i" % (vertice, grau_do_vertice))

  



#saber se o grafo é regular usando a biblioteca
if nx.is_regular(G):
  print('eh regular')
else:
  print('nao é regular')



#saber se eh regular usando a def
def eh_regular(grafo):
  vertices_ = list(grafo.nodes)
  grau_inicial = grau_vertice(grafo, vertices_[0])

  for vertice in vertices_[1:]:
    if grau_vertice(grafo, vertice) != grau_inicial:
      return False
    
  return True
    



print(eh_regular(G))




resposta = (input('exibir grafo [s] [n]'))
if resposta == 's':
  exibir_grafo(G)
else:
  print('ok')





