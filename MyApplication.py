from kivy.app import App
#from kivy.uix.pagelayout import PageLayout
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import Image


# ANCHOR LAYOUT
'''
class MyApp(App):

	def build(self):
		layout = AnchorLayout(
			anchor_x = 'left',
			anchor_y = 'top')
		button1 = Button(
			text = "Just a widget",
			size_hint = (0.2,0.2),
			background_color = (125, 255, 159),
			color = (125, 255, 159)
			)
		layout.add_widget(button1)
		return layout
'''

# GRID LAYOUT
'''
class GridLayoutDemo(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.row = 2
		self.cols = 2

		self.l1 = Label(
			text = "Click me!"
		)
		self.add_widget(self.l1)

		self.b1 = Button(
			text = "Click me!",
			background_color = (0,24,67),
			color = (0,0,0)
		)
		self.add_widget(self.b1)


class MyApp(App):
	def build(self):
		return GridLayoutDemo()
'''

# FLOAT LAYOUT
'''
class FLoatLayoutDemo(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.b1 = Button(
			text = "Button test",
			size_hint = (0.3, 0.3),
			pos_hint = {"x": 0.3, "y": 0.6}
		)
		self.add_widget(self.b1)

		self.b2 = Button(
			text = "Button 2",
			size_hint = (0.1, 0.2),
			pos_hint = {"x": 0.9, "y": 0.8}
		)
		self.add_widget(self.b2)


class MyApp(App):
	def build(self):
		return FLoatLayoutDemo()
'''

# PAGE LAYOUT
'''
class PageLayoutDemo(PageLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.b1 = Button(
			text = "Button1"
		)
		self.add_widget(self.b1)

		self.b2 = Button(
			text="Button2"
		)
		self.add_widget(self.b2)

		self.b3 = Button(
			text="Button3"
		)
		self.add_widget(self.b3)

class MyApp(App):
	def build(self):
		return PageLayoutDemo()
'''


class KivyUI(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 4

        self.img = Image(
            source = "C:/Users/PC/Pictures/2019-11/twirlBG - Copy-2.jpg"
        )
        self.add_widget(self.img)

        self.l1 = Label(
            text = "Enter you name"
        )
        self.add_widget(self.l1)

        self.txt = TextInput(
            text = "do smth",
            font_size = 30
        )
        self.add_widget(self.txt)

        self.bttn = Button(
            text = "Submit"
        )
        self.bttn.bind(on_press = self.call_back)
        self.add_widget(self.bttn)

        self.pop = Popup(
            title = "POP-UP displayed",
            size_hint = (0.5,0.3),
            content = Label(
                text = ""
            )
        )

    def call_back(self, elem):
        self.pop.content.text = self.txt.text
        self.pop.open()

class MyApp(App):
    def build(self):
        return KivyUI()

MyApp().run()