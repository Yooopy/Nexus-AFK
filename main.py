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

        return Builder.load_file("loader.kv")

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