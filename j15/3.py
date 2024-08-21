from tkinter import *

def on_key(event):
    print(f"Key pressed: {event.char}")


root = Tk()


root.bind("<Key>", on_key)
root.mainloop()  # Start the main event loop
