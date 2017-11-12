#-*-coding:utf-8-*-
'''
@author: Israël & Renan
@note: Implementação do algoritmo de Prim
'''
from random import choice
from plot import Plot
grafo={
  '0':{'2':5,'3':8},
  '1':{'2':16,'4':30,'6':26},
  '2':{'0':5,'3':10,'4':3,'1':16},
  '3':{'0':8,'2':10,'4':2,'5':18},
  '4':{'2':3,'3':2,'5':12,'6':14,'1':30},
  '5':{'3':18,'4':12,'6':14},
  '6':{'1':26,'4':14,'5':4}
}
#coordenadas dos vértices
pos={
  '0':(50,100),
  '1':(200,50),
  '2':(100,50),
  '3':(100,150),
  '4':(150,100),
  '5':(200,150),
  '6':(250,100)
  }

global T#variável global de escolha do vértice
T=[]
lst=[x for x in grafo]
i=choice(lst)
T.append(i)
global V
V = [x for x in lst if x!=i]
global Tmin
Tmin = []
while len(T)!=len(lst):
  menor=1000000
  p=None
  q=None
  for j in T:
    for k in V:
      if k in grafo[j]:
        print("Procurando custo da aresta ({},{})".format(j,k))
        if grafo[j][k]<menor:
          print("Aresta de menor custo: ({},{})".format(j,k))
          menor=grafo[j][k]
          p=j
          q=k
  T.append(q)
  V=[x for x in V if x!=q]
  Tmin.append((p,q))
print(Tmin)
pl=Plot(Tmin,pos)
pl.plot("Árvore geradora mínima")
