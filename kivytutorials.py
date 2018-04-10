'''

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

class HelloKivyApp(App):

    def build(self):
        return Label()

helloKivy = HelloKivyApp()

helloKivy.run()
'''


'''
# Static layout for Kivy
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

customWidget = CustomWidgetApp()
customWidget.run()

'''

'''
# Float layout for Kivy
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class FloatingApp(App):

    def build(self):
        return FloatLayout()

flApp = FloatingApp()
flApp.run()
'''

# Grid layout for Kivy
