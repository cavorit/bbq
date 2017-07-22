#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.widget import Widget

class PongGames(Widget):
    pass

class PongApp(App):

    def build(self):

        return PongGame()

if __name__ == '__main__':
    PongApp().run()


