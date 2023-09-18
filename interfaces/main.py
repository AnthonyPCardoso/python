import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text="Botão 1", font_size=30,on_release=self.incrementar)
        self.label = Label(text= ' 1', font_size = 30)
        box.add_widget(button)
        box.add_widget(self.label)
        return box
    

    def incrementar(self,button):
        button.text='Soltei'
        self.label.text = str(int(self.label.text)+ 1)


if __name__ == "__main__":
    MyApp().run()