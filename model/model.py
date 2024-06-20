import copy
from math import sqrt
#from geopy.distance import geodesic

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.idMapTeams = {}


    def getTeams(self):
        squadre = DAO.getAllTeams()
        for s in squadre:
            self.idMapTeams[s[0]] = s[1]

    def buildGraph(self, team):
        pass



