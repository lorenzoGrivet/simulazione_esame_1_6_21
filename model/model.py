import copy
import random
from math import sqrt
#from geopy.distance import geodesic

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo= nx.Graph()
        self.idMap={}
        self.gene=None
        self.dizGeni={}
        pass

    def creaGrafo(self):
        self.grafo.clear()
        nodi=DAO.getGene()
        self.grafo.add_nodes_from(nodi)
        for a in nodi:
            self.idMap[a.GeneID]=a
        archiUguali=DAO.getArchiUguali()
        archiDiversi=DAO.getArchiDiversi()
        for a in archiUguali:
            self.grafo.add_edge(self.idMap[a[0]],self.idMap[a[1]],peso=float(a[2]))
        for a in archiDiversi:
            self.grafo.add_edge(self.idMap[a[0]],self.idMap[a[1]],peso=float(a[2]))

        return nodi

    def getAdiacenti(self,nodo):
        succ= list(self.grafo.edges(nodo,data=True))
        vicini= sorted(succ,key= lambda x: x[2]["peso"],reverse=True)
        return vicini

    def getDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

    def cammino(self,nodo,ing):


        # self.gene=nodo
        for a in self.grafo.nodes:
            self.dizGeni[a]=0
        self.dizGeni[nodo]=ing

        for p in range(36):

            for geneSel in self.dizGeni.keys():
                if self.dizGeni[geneSel]!=0:

                    # lista=[0,0,0,1,1,1,1,1,1,1]
                    # prob=random.choice(lista)
                    self.dizGeni[nodo]=0.3*ing

                    succ=list(self.grafo.neighbors(geneSel))
                    somma=0
                    for s in succ:
                        somma+=self.grafo[geneSel][s]["peso"]
                    for a in succ:
                        self.dizGeni[a] = self.dizGeni[geneSel]*self.grafo[geneSel][a]["peso"]/somma
        return self.dizGeni




