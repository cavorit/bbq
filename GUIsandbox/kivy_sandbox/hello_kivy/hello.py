#!/usr/bin/env python3.3

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):     # 1-st step: sub-classing the APP class
    def build(self):    # 2-nd step: implementing its build() method so it returns a *widget* instance (the root of your widget tree)
        return Button(text='Hello World')

TestApp().run()         # 3-rd step: instanting this class, and calling its run() method.

