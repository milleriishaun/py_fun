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
'''


'''
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):
    
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()
'''

'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class StudentListButton(ListItemButton):
    pass

class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_students(self):
        pass

    def delete_student(self):
        pass
    
    def replace_student(self):
        pass
    
class StudentDBApp(App):
    def build(self):
        return StudentDB()
    
dbApp = StudentDBApp()
dbApp.run()
'''


'''
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class SampGridLayout(GridLayout):
    pass

class SampleApp(App):
    def build(self):
        return SampGridLayout()

sample_app = SampleApp()
sample_app.run()
'''

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

class CustomPopup(Popup):
    pass

class SampBoxLayout(BoxLayout):

    checkbox_is_active = ObjectProperty(False)

    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Not Clicked")
    
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    def switch_on(self, instance, value):
        if value is True:
            print("Switch On")
        else:
            print("Switch Off")
    
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()
    
    def spinner_clicked(self, value):
        print("Spinner Value: " + value)

class SampApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return SampBoxLayout()

sample_app = SampApp()
sample_app.run()