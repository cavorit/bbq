from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

class haraldRootWidget(BoxLayout):
    def choices(self, guess):
        output = 'You clicked the '+guess+' button!'
        self.ids.myResults.text=output



class mySuperApp(App):
    def build(self):
        return haraldRootWidget()

if __name__ == "__main__":
    mySuperApp().run()


