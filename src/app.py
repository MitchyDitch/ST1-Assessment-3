from doctest import master
import tkinter as tk


class GUI:
    def __init__(self):

        self.label = tk.Label(master, text="Hello, World!")
        self.label.pack()

        self.button = tk.Button(master, text="Click Me", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button Clicked!")
