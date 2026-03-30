# Modern Hello World - Python Edition

This project is a simple demonstration of building a Graphical User Interface (GUI)
using Python. Instead of a standard console log, this app renders a styled window.

## How to Run

1. Install Python 3.
2. Run `pip install customtkinter`.
3. Run `python main.py`.

# A simple reusable toolkit for starting GUI projects

import customtkinter as ctk

def create_base_window(title, width=400, height=300):
"""Returns a pre-styled modern window object."""
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title(title)
app.geometry(f"{width}x{height}")
return app

def add_header(master, text):
"""Adds a standard styled header to any window."""
label = ctk.CTkLabel(master=master, text=text, font=("Arial", 20, "bold"))
label.pack(pady=20)
return label
