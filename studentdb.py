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

    def submit_student(self):
        # Get the student's name from text inputs
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
        # Add the student to listview
        self.student_list.adapter.data.extend([student_name])
        # Reset the listview
        self.student_list._trigger_reset_populate()

    def delete_student(self):
        # if a listbutton is selected
        if self.student_list.adapter.selection:
            # if one of them is selected, want to get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
            # remove the matching item from the listview
            self.student_list.adapter.data.remove(selection)

            # reset the list view
            self.student_list._trigger_reset_populate()
    
    def replace_student(self):
        # if a listbutton is selected
        if self.student_list.adapter.selection:
            # get the text of the list item
            selection = self.student_list.adapter.selection[0].text
            # remove the matching item
            self.student_list.adapter.data.remove(selection)
            # Get the student name from the input
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
            # add the updated data to the listview
            self.student_list.adapter.data.extend([student_name])
            # reset the listview
            self.student_list._trigger_reset_populate()
    
class StudentDBApp(App):
    def build(self):
        return StudentDB()
    
dbApp = StudentDBApp()
dbApp.run()