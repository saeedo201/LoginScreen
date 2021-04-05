from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation

Kv = """
MDScreen:
    name: "LoginPage"
    on_enter:
        app.anim(back)
        app.anim1(back1)
        app.icons(icon)
        app.text(label)
        
    MDFloatLayout:       
        MDFloatLayout:
            id: back
            size_hint_y:.8
            pos_hint:{'center_y': 1.8}
            radius: [0,0,0,40]
            canvas:
                Color:
                    rgb: (1,0,0, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos
                    
        MDFloatLayout:
            id: back1
            size_hint_y:.6
            pos_hint:{'center_y': 1.8}
            radius: [0, 0, 0, 40]
            canvas:
                Color:
                    rgb: (1,0,0, 1)
                Ellipse:
                    size: self.size
                    pos: self.pos
                    
        MDIconButton:
            id: icon
            icon: "account-circle"
            pos_hint: {"center_x":.5, "center_y":.8}
            user_font_size: "60sp"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            
        MDLabel:
            id: label
            text: "Login page"
            markup: True
            pos_hint: {"center_y":.75}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            font_style: "H5"
            opacity: 0
            
        MDTextField:
            hint_text: "Email"
            icon_right: "email"
            size_hint_x: None
            pos_hint: {"center_x":.5, "center_y": .54}
            current_hint_text_color: 0, 0, 0, 1
            color_text: "Custom"
            line_color_focus: 1, 0, 0, 1
            width: 700
            
        MDTextField:
            hint_text: "Password"
            icon_right: "login"
            size_hint_x: None
            pos_hint: {"center_x":.5, "center_y": .46}
            current_hint_text_color: 0, 0, 0, 1
            password: True
            color_text: "Custom"
            line_color_focus: 1, 0, 0, 1
            width: 700
            
        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": .5, "center_y": .4}
            size_hint_x: .5
            md_bg_color: 1, 0, 0, 1
            
        MDLabel:
            text: "Did you"
            pos_hint: {"center_x": .672, "center_y": .3}
            font_style: "Body2"
            
        MDTextButton:
            text: "forget your password?"
            pos_hint: {"center_x": .68, "center_y": .3}
            custom_color: 1, 0, 0, 1              
"""

class LoginApp(MDApp):
    def change_screen(self, name):
        screen_manager.current = name
        
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(Kv))
        return screen_manager
        
    def anim(self, widget):
        anim = Animation(pos_hint={"center_y": 1.16})
        anim.start(widget)
        
    def anim1(self, widget):
        anim = Animation(pos_hint={"center_y": .90})
        anim.start(widget)
        
    def icons(self, widget):
        anim = Animation(pos_hint={"center_y": .8})
        anim += Animation(pos_hint={"center_y": .90})
        anim.start(widget)
        
    def text(self, widget):
        anim = Animation(opacity=0, duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)
        
if __name__ == '__main__':
    app = LoginApp()
    app.run()
