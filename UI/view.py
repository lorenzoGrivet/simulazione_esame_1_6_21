import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddyear = None
        self.ddshape = None
        self.btn_graph = None
        self.txt_result = None
        self.txt_container = None

        self.txtN = None
        self.txtOut2 = None
        self.btn_path = None


    def load_interface(self):
        # title
        self._title = ft.Text("simulazione esame 1/6/21", color="blue", size=24)
        self._page.controls.append(self._title)

        #row 1
        self.ddGene = ft.Dropdown(label="Scegli un gene")
        self.btn_graph = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_crea_grafo)

        row1 = ft.Row([ft.Container(self.ddGene, width=300),ft.Container(self.btn_graph, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        # self._controller.fillDDTeams()

        self.txtIng= ft.TextField(label="Numeri ingegneri: ")
        self.btn_simulazione=ft.ElevatedButton(text="Simulazione",on_click=self._controller.handle_simulazione)

        row2=ft.Row([ft.Container(self.txtIng,width=300),ft.Container(self.btn_simulazione,width=300)],alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
