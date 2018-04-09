from tkinter import *
from PIL import Image, ImageTk

class TkInterEx:

    @staticmethod
    def quit_app(event=None):
        root.quit()

    def on_fav_food_select(self, event=None):
        lb_widget = event.widget # get widget that triggered event
        # set up everything with indexes
        index = int(lb_widget.curselection()[0]) # index of listbox

        lb_value = lb_widget.get(index)

        # just change the label depending on what the user selects
        self.fav_food_label['text'] = "I'll get you " + lb_value

    def __init__(self, root):
        root.title("Toolbar Example")
        menubar = Menu(root)

        file_menu = Menu(root, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Exit", command=self.quit_app)

        menubar.add_cascade(label="File", menu=file_menu)

        # Create the toolbar
        toolbar = Frame(root, borderwidth=1, relief=RAISED)

        open_img = Image.open("open.png").resize((50, 50))
        save_img = Image.open("save.png").resize((50, 50))
        exit_img = Image.open("exit.png").resize((50, 50))

        # create the tkinter image for the buttons
        open_icon = ImageTk.PhotoImage(open_img)
        save_icon = ImageTk.PhotoImage(save_img)
        exit_icon = ImageTk.PhotoImage(exit_img)

        # create teh buttons for the toolbar
        open_button = Button(toolbar, image=open_icon)
        save_button = Button(toolbar, image=save_icon)
        exit_button = Button(toolbar, image=exit_icon, command=self.quit_app)

        # add the image onto the button, in the image position
        open_button.image = open_icon
        save_button.image = save_icon
        exit_button.image = exit_icon

        # show all this stuff
        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        exit_button.pack(side=LEFT, padx=2, pady=2)

        # create toolbar
        toolbar.pack(side=TOP, fill=X)
        # connect menubar
        root.config(menu=menubar)

        # make a label frame
        lb_frame = LabelFrame(root, text="Food Options", padx=5, pady=5)

        self.fav_food_label = Label(lb_frame, text="What is your favorite food?")

        self.fav_food_label.pack()

        list_box = Listbox(lb_frame)

        # insert the listbox options
        list_box.insert(1, "Spaghetti")
        list_box.insert(2, "Pizza")
        list_box.insert(3, "Burgers")
        list_box.insert(4, "Hot Dogs")

        # tie an event to the function
        # this connects clicked selection to function call
        list_box.bind('<<ListboxSelect>>', self.on_fav_food_select)

        list_box.pack()

        lb_frame.pack()


        # create the spinbox frame
        sb_frame = Frame(root)

        quantity_label = Label(sb_frame, text="How may do you want?")
        quantity_label.pack()

        spin_box = Spinbox(sb_frame, from_=1, to=5)
        spin_box.pack()

        extras_label = Label(sb_frame, text="Add on Item")
        extras_label.pack()

        extras_spin_box = Spinbox(sb_frame, 
                                values=('French Fries',
                                'Onion Rings',
                                'Tater Tots'))
        extras_spin_box.pack()

        sb_frame.pack()

    
root = Tk()
root.geometry("600x550")
app = TkInterEx(root)
root.mainloop()