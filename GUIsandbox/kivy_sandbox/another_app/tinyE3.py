#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class meinRootWidget(GridLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.cols = 3
        for i in range(1,7):
            self.add_widget(Label(text=str(i)))

class MyApp(App): # sub-classing APP class

    def build(self): # implement its build() method

        return meinRootWidget() # return the root of Widget tree
            
if __name__ == "__main__":
    MyApp().run()



