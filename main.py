import sys
import time
import webbrowser
from threading import Timer
import ctypes
import pyautogui
import win32api, win32con, win32gui
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.metrics import sp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)
from kivymd.uix.widget import Widget
from kivymd.uix.label import MDLabel



def ctypes_movement(x, y):
    ctypes.windll.user32.mouse_event(0x0001, x, y, 0, 0)



class MainApp(MDApp):
    def build(self):
        self.icon = 'ahaa.png'
        self.title = 'NEXUS AFK'
        Window.minimum_width, Window.minimum_height = 800,600
        self.theme_cls.primary_palette = 'Lightseagreen'
        self.theme_cls.theme_style = 'Dark'
        #Font ==>
        LabelBase.register(
            name="nasalization",
            fn_regular="nasalization.ttf",
        )

        self.theme_cls.font_styles["nasalization"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "nasalization",
                "font-size": sp(57),
            },
            "medium": {
                "line-height": 1.52,
                "font-name": "nasalization",
                "font-size": sp(45),
            },
            "small": {
                "line-height": 1.1,
                "font-name": "nasalization",
                "font-size": sp(14),
            }
        }  #<==

        return Builder.load_string('''#: import webbrowser webbrowser
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    MDCard:
        spacing: 10
        padding: 40
        orientation: 'vertical'
        theme_bg_color: "Custom"
        md_bg_color: '#232323'
        style: 'elevated'
        theme_elevation_level: "Custom"
        elevation_level: 4
        size_hint: (0.85,0.85)
        theme_shadow_softness: "Custom"
        shadow_softness: 5
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        MDLabel:
            valign: 'middle'
            text: 'Nexux Afk Bot'
            halign: 'center'
            font_style: 'nasalization'
            role: 'medium'
            size_hint: 1,0.2
        MDLabel:
            id: textt
            text: 'How many minutes do you want to use this?'
            size_hint: 1,None
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDDivider:

            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5,}
        Widget:
            size_hint_y: None
            height: 10

        MDCard:
            orientation: 'horizontal'
            radius: [20]
            spacing: 15
            padding: 15
            style: 'elevated'
            size_hint: 0.95,None
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            theme_bg_color: "Custom"
            md_bg_color: '#282828'
            MDTextField:
                id: t_field
                radius: [20]

                MDTextFieldHintText:
                    bold: True
                    text: 'Minutes:'
            MDButton:
                style: 'filled'
                height: 70
                radius: 20
                on_release: app.event()

                MDButtonText:
                    text: 'Start'
                    font_style: 'Title'
                    role: 'large'
#        Widget:
#            size_hint_y: None
        MDButton:
            style: 'text'
            on_release: webbrowser.open('https://github.com/Yooopy/NEXUSAFK/raw/6693b959869369dbf7f064fcf8f5f8f7e1cd9b42/Hint.txt')
            MDButtonText:

                text: 'How it Works?'
        BoxLayout:
            spacing: 10
            padding: 0
            pos_hint: {'center_x': 0.5}
            size_hint: None,None
            orientation: 'horizontal'
            MDIconButton:
                icon: 'github'
                on_release: webbrowser.open('https://github.com/Yooopy/NEXUSAFK')
            MDDivider:
                orientation: 'vertical'
                size_hint_y: 0.5
            MDIconButton:
                on_release: app.email_dialog()
                icon: 'yahoo'

    MDLabel:
        text: 'Made By V | 2024'
        halign: 'center'
        size_hint: 1,None
        font_style: 'nasalization'
        role: 'small'
        theme_text_color: "Custom"
        text_color: '#404040'
        pos_hint: {'center_x': 0.5,'center_y': 0.03}

''')

    def email_dialog(self):
        MDDialog(
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="yahoo",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="vgeraph@yahoo.com",
            )).open()
    def mouse_rotate(self):
        ctypes_movement(300, 0)
        time.sleep(0.5)
        ctypes_movement(0, 300)
        time.sleep(0.5)
        ctypes_movement(-300, 0)
        time.sleep(0.5)
        ctypes_movement(0, -300)
        x1, y1 = pyautogui.size()
        x1, y1 = int(x1 / 2), int(y1 / 2)
        win32api.SetCursorPos((x1, y1))
    def nothing(self):
        a = 2

    def q_click(self):
        pyautogui.press('Q', presses=6, interval=0.5)

    def mouse_click(self):
        b = Timer(2, lambda: self.nothing())
        b.start()
        pyautogui.mouseDown(960,560,button='left')
        pyautogui.mouseUp(960,560,button='left')

        while b.is_alive():
            pyautogui.mouseDown(960,560,button='left')
        else:
            pyautogui.mouseUp(960,560,button='left')

    def movement(self):
        tq = Timer(1, lambda: self.nothing())
        tq.start()
        while tq.is_alive():
            pyautogui.keyDown(key='A')
        else:
            pyautogui.keyUp(key='A')
        tqq = Timer(1, lambda: self.nothing())
        tqq.start()
        while tqq.is_alive():
            pyautogui.keyDown(key='S')
        else:
            pyautogui.keyUp(key='S')
        tww = Timer(1, lambda: self.nothing())
        tww.start()
        while tww.is_alive():
            pyautogui.keyDown(key='D')
        else:
            pyautogui.keyUp(key='D')
        tee = Timer(1, lambda: self.nothing())
        tee.start()
        while tee.is_alive():
            pyautogui.keyDown(key='W')
        else:
            pyautogui.keyUp(key='W')

    def space_and_r(self):
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        pyautogui.keyDown('R')
        pyautogui.keyUp('R')
        time.sleep(1)
    def event(self):
        try:
            timee = float(self.root.ids.t_field.text)
            timee *= 60
            main_timer = Timer(timee, lambda: sys.exit())
            Window.minimize()
            time.sleep(10)
            main_timer.start()
            while main_timer.is_alive():
                self.q_click()
                time.sleep(0.5)
                self.mouse_click()
                time.sleep(0.5)
                self.mouse_rotate()
                time.sleep(0.5)
                self.movement()
                time.sleep(0.5)
                self.space_and_r()
        except pyautogui.FailSafeException:
            sys.exit()

if __name__ == '__main__':
    MainApp().run()