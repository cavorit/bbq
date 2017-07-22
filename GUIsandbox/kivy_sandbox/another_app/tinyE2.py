#!/usr/bin/env python3.3
# a minimal application

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
#        self.username = TextInput(multiline=False)
#        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
#        self.password = TextInput(password=True, multiline=False)
#        self.add_widget(self.password)
        self.add_widget(Label(text='Hallo Jojo'))
        self.add_widget(Label(text='D'))
        self.add_widget(Label(text='E'))
        self.add_widget(Label(text='F'))
        self.add_widget(Label(text='G'))       


class MyApp(App):    #sub-classing APP class


    def build(self): #implementing its build() method
                     #so it returns the root of the widget tree
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run() #instance this calls and call its run() method.

