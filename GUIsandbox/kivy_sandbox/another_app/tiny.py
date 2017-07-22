#!/usr/bin/env python3.3
# a minimal application

import kivy
kivy.require('1.10.0') 

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):    #sub-classing APP class
    def build(self): #implementing its build() method
                     #so it returns the root of the widget tree
        return Label(text='Hello World')

if __name__ == '__main__':
    MyApp().run() #instance this calls and call its run() method.

