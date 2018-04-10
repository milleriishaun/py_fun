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


'''
# Grid layout for Kivy
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class GridLayoutApp(App):

    def build(self):
        return GridLayout()

glApp = GridLayoutApp()
glApp.run()
'''

'''
# Box layout for Kivy
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutApp(App):

    def build(self):
        return BoxLayout()

blApp = BoxLayoutApp()
blApp.run()
'''

'''
# Stack layout for Kivy
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.stacklayout import StackLayout


class StackLayoutApp(App):

    def build(self):
        return StackLayout()

slApp = StackLayoutApp()
slApp.run()
'''

# Page layout for Kivy
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.pagelayout import PageLayout


class PageLayoutApp(App):

    def build(self):
        return PageLayout()

plApp = PageLayoutApp()
plApp.run()