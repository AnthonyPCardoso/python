import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self,tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size = 20, size_hint_y = None, height = 200))
        


class Toque(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Buscar filho', 'Molhar a calçada', 'ksao', 'oidao', 'ldpas', 'plas', 'plasp'])
    
Toque().run()