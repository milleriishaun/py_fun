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
'''


import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<ScreenOne>:
    BoxLayout:
        Button:
            text: "Go to Screen 2"
            on_press: 
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_two"
                
<ScreenTwo>:
    BoxLayout:
        Button:
            text: "Go to Screen 1"
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 1
                root.manager.current = "screen_one"
""")

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

screen_manager = ScreenManager()

screen_manager.add_widgest(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))

class KivyTut2App(App):
    def build(self):
        return screen_manager

sample_app = KivyTut2App()
sample_app.run()

# I learned Django after this, and that was good for learning about
# web frameworks and really what people are looking for.
# After learning Django, I found out that people are looking for MEAN stack and
# MERN stack. Now that I have a working part of the MEAN stack but am not finding
# too many structured tutorials, I am kind of bogged down. I can learn it though.
# What I'll try to do is learn the MEAN stack enough to get things moving,
# but not learn it so well that I can only use it. I will need to stick with MEAN and MERN
# for about 2 weeks and learn all that I can about them in that time.
# Once it is finished and I have some work that I can show, I want to dive into other tutorials.
# I want to get the hackrank stuff in. I want to try. Also I want that certificate from freecodecamp.
# Other than that, I want to develop that app for the church that we've been talking about.
# Another thing I can do is find the documentations for individual MEAN?MERN pieces to know more in depth.
# Another thing I can do is practice typing and practice writing out the code so it works. THis would be python.
# I can focus on software development, while continuing with software engineering(trying to connect everything).
# I should think what I will be hired to do: JAVA with the Spring framework(these are big companies hiring, so need CS degree)
# ... or Kotlin for Android. PHP 7 is powerful right now(also king od freelance... with Laravel/Symphony), 80% of businesses, apps like Facebook. IBM took on Swift(really fast), just ios apps.
# not server-side. I could also learn CRUD operations with Databases even faster and more efficiently.
# C# with web apps... fast games(UNITY) using asp.NET framework(mainly working for a company). Common for Microsoft projects. 
