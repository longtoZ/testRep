from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('changer.kv')

class GridTest(Widget):
    nameInput = ObjectProperty(None)
    emailInput = ObjectProperty(None)


    def bttn(self):
        print("Name: ", self.nameInput.text, "Email: ", self.emailInput.text)
        self.nameInput.text = ""
        self.emailInput.text = ""
        
    '''
    def on_touch_down(self, touch):
        self.button.opacity = 0.5
        # self.button.background_color = 166, 123, 114
    def on_touch_up(self, touch):
        self.button.opacity = 1
    '''

class ChangerApp(App):
    def build(self):
        return GridTest()

ChangerApp().run()