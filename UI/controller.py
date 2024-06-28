import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.nodi = None
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model
        self.selectedGene=None

    def fillDD(self,nodi):
        nodiDD= list(map(lambda x: ft.dropdown.Option(key=x.GeneID,data=x,on_click=self.getSelectedGene), nodi))
        self.view.ddGene.options=nodiDD
        self.view.update_page()

    def handle_crea_grafo(self, e):
        self.nodi=self.model.creaGrafo()
        n,a= self.model.getDetails()
        self.view.txt_result.controls.append(ft.Text(f"Nodi: {n}. Archi: {a}"))
        self.view.update_page()

        self.fillDD(self.nodi)
        pass

    def handle_geni_adiacenti(self, e):
        vicini= self.model.getAdiacenti(self.selectedGene)
        self.view.txt_result.controls.append(ft.Text(f"Vicini di {self.selectedGene}"))
        for a in vicini:
            self.view.txt_result.controls.append(ft.Text(f"{a[1]}, peso = {a[2]["peso"]}"))
        self.view.update_page()

    def handle_simulazione(self, e):
        self.model.cammino(self.selectedGene,int(self.view.txtIng.value))
        pass


    def getSelectedGene(self, e):
        if e.control.data is None:
            pass
        else:
            self.selectedGene=e.control.data