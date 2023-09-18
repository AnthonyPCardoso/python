import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class incrementador(BoxLayout):
    ...

class Test(App):
    def build(self):
        return incrementador()
    

    def incrementar(self,button):
        self.label.text = str(int(self.label.text)+1)

if __name__ == "__main__":
    Test().run()