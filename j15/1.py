from tkinter import *
from tkinter import ttk, messagebox, filedialog


# Define the main application
class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Widgets Demo")
        self.geometry("600x600")

        # Create a menu
        self.create_menu()

        # Create a label
        self.label = Label(self, text="This is a Label", font=("Arial", 14))
        self.label.pack(pady=10)

        # Create an Entry
        self.entry = Entry(self, width=30)
        self.entry.insert(0, "Type something here...")
        self.entry.pack(pady=10)

        # Create a Text box
        self.text = Text(self, height=4, width=40)
        self.text.insert(
            END, "This is a Text widget.\nYou can enter multiple lines of text."
        )
        self.text.pack(pady=10)

        # Create Checkbuttons
        self.check_var1 = IntVar()
        self.check_var2 = IntVar()
        self.checkbutton1 = Checkbutton(
            self, text="Option 1", variable=self.check_var1
        )
        self.checkbutton2 = Checkbutton(
            self, text="Option 2", variable=self.check_var2
        )
        self.checkbutton1.pack(pady=5)
        self.checkbutton2.pack(pady=5)

        # Create Radiobuttons
        self.radio_var = IntVar()
        self.radiobutton1 = Radiobutton(
            self, text="Choice 1", variable=self.radio_var, value=1
        )
        self.radiobutton2 = Radiobutton(
            self, text="Choice 2", variable=self.radio_var, value=2
        )
        self.radiobutton1.pack(pady=5)
        self.radiobutton2.pack(pady=5)

        # Create a Listbox
        self.listbox = Listbox(self)
        self.listbox.insert(1, "Item 1")
        self.listbox.insert(2, "Item 2")
        self.listbox.insert(3, "Item 3")
        self.listbox.pack(pady=10)

        # Create a Combobox
        self.combobox = ttk.Combobox(self, values=["Option 1", "Option 2", "Option 3"])
        self.combobox.current(2)
        self.combobox.pack(pady=10)

        # Create a Canvas for drawing
        self.canvas = Canvas(self, width=200, height=100, bg="lightgray")
        self.canvas.create_line(0, 0, 200, 100, fill="blue")
        self.canvas.create_rectangle(50, 25, 150, 75, fill="red")
        self.canvas.pack(pady=10)

        # Create a Button
        self.button = Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def create_menu(self):
        # Create a menu bar
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        # Create a File menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Create a Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def on_button_click(self):
        messagebox.showinfo("Button Clicked", "You clicked the button!")

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path:
            messagebox.showinfo("File Selected", f"File: {file_path}")

    def show_about(self):
        messagebox.showinfo("About", "This is a Tkinter widget demo.")


# Run the application

app = MyApp()
app.mainloop()
