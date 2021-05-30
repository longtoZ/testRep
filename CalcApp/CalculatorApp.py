from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation


Window.size = (400,600)
kv = Builder.load_file('calculator.kv')

class MyLayout(Widget):
    def buttonAnimation(self, widget):
        anim = Animation(
            font_size = 25*1.5,
            duration= .1) + Animation(
            font_size=25,
            duration=.2
            )

        anim.start(widget)

    def operatorButtonAnimation(self, widget):
        anim = Animation(
            font_size = 25*1.5,
            duration= .1) + Animation(
            font_size=25,
            duration=.2
            )

        anim.start(widget)

class CalculatorApp(App):
    def build(self):
        return MyLayout()

CalculatorApp().run()