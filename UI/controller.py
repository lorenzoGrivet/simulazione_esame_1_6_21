import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDTeams(self):
        self._model.getTeams()
        teams = self._model.idMapTeams
        teamsDD = list(map(lambda x: ft.dropdown.Option(text=teams[x], key=x), teams))
        self._view.ddTeams.options = teamsDD
        self._view.update_page()




    def handle_crea_grafo(self, e):
        self.squadra = self._view.ddTeams.value
        if self.squadra is None:
            self._view.txt_result.controls.append(ft.Text(f"Squadra non selezionata"))
            return

        self._model.buildGraph(self.squadra)





