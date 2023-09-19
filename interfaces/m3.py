import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self,tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
        

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
    

class Toque(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Buscar filho', 'Molhar a calçada', 'ksao', 'oidao', 'ldpas', 'plas', 'plasp'])
    

if __name__ == "__main__":
    Toque().run()