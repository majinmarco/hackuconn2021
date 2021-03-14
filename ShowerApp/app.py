import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ClockDemo(App):
    count = 0

    def build(self):
        b = BoxLayout(orientation = 'vertical')

        t = TextInput(font_size = 50,
                      size_hint_y = None,
                      height = 100)

        f = FloatLayout()
        s = Scatter()

        self.myLabel = Label(text = 'Waiting on updates...')

        Clock.schedule_interval(self.Callback_Clock, 1)

        return self.myLabel 

    def Callback_Clock(self, dt):
        self.count = self.count+1
        self.myLabel.text = f"Updated {self.count} times"

if __name__ == "__main__":
    ClockDemo().run()   