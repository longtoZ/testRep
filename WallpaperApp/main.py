from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.lang import Builder

string = '''
<MyLayout>
    bttn1: bttn1
    ScrollView:
        size: root.width, root.height
        
        MDFloatLayout:
            size: root.width, root.height
            #radius: [25, 0, 0, 0]
            
            
            MDRoundFlatButton:
                id: bttn1
                #icon: "android"
                text: "A bruh button"
                font_size: '15dp'
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint : (.9,.2)
                on_press: root.buttonPress()
            
            MDRoundFlatButton:
                id: bttn2
                #icon: "android"
                text: "A bruh button"
                font_size: '15dp'
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint : (.9,.2)
                on_press: root.buttonPress()
                

'''

kv = '''
<MyLayout>
    FloatLayout:
        size: root.width, root.height
        
        MDToolbar:
            title: "Wallpaper Changer"
            right_action_items: [["dots-vertical", lambda x: root.callback1()]]
            size_hint: (1,.1)
            pos_hint: {'y':.9}
                
        ScrollView:
            size_hint: (1,1)
            pos_hint: {'top':.9}
            
            MDList:
                
            
                TwoLineAvatarIconListItem:               
                    text: "Unplash"
                    
                    secondary_text: "Secondary text here"            
                    IconLeftWidget:
                        icon: "plus"
                
                TwoLineAvatarIconListItem:               
                    text: "Unplash"
                    
                    secondary_text: "Secondary text here"            
                    IconLeftWidget:
                        icon: "plus"
                
                TwoLineAvatarIconListItem:               
                    text: "Unplash"
                    
                    secondary_text: "Secondary text here"            
                    IconLeftWidget:
                        icon: "plus"
                
                TwoLineAvatarIconListItem:               
                    text: "Unplash"
                    
                    secondary_text: "Secondary text here"            
                    IconLeftWidget:
                        icon: "plus"
                TwoLineAvatarIconListItem:               
                    text: "Unplash"
                    
                    secondary_text: "Secondary text here"            
                    IconLeftWidget:
                        icon: "plus"
                
                TwoLineAvatarIconListItem:               
                    text: "Unplash"
                    
                    secondary_text: "Secondary text here"            
                    IconLeftWidget:
                        icon: "plus"
                
'''

Builder.load_string(kv)
Window.size = (400,600)

class MyLayout(Widget):
    bttn1 = ObjectProperty(None)
    def buttonPress(self):
        self.bttn1.text = 'Text changed'

    def callback1(self):
        pass


class WallpaperApp(MDApp):
    def build(self):
        self.theme_cls.accent_palette = 'Teal'
        return MyLayout()

if __name__ == "__main__":
    WallpaperApp().run()