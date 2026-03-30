# Building a Stylized "Hello World" with Python and CustomTkinter

Technology Chosen: Python (specifically using the CustomTkinter library).

Why I chose it: I wanted to move beyond the boring black-and-white terminal. Python is famous for being beginner-friendly, and CustomTkinter allows for a modern, dark-mode-ready UI with very little code.

End Goal: Create a desktop window that displays "Hello World" with a modern button and a sleek, rounded aesthetic.

# Quick Summary of the Technology

What is it? Python is a high-level, interpreted programming language known for readability. CustomTkinter is a wrapper around Python's built-in GUI library (Tkinter) that provides consistent, modern-looking components across different OS platforms.

Where is it used? It's used for building lightweight desktop tools, internal company dashboards, and simple data visualization apps.

Real-world example: Many simple system utilities or "cleaner" apps on Windows/macOS use similar GUI frameworks.

# System Requirements

OS: Windows, macOS, or Linux.

Tools/Editors: VS Code or PyCharm.

Environment: Python 3.7 or higher installed.

Packages: customtkinter (installed via pip).

# Installation & Setup Instructions

Check Python version:

Bash
python --version
Install the UI Library:
Open your terminal/command prompt and run:

Bash
pip install customtkinter
Minimal Working Example
This script creates a modern window with a centered "Hello World" message and a button.

Python
import customtkinter as ctk

# Function to handle button click

def say_hello():
print("Button was clicked!")

# 1. System Settings (The 'Look and Feel')

ctk.set_appearance_mode("dark") # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

# 2. Initialize the App

app = ctk.CTk()
app.geometry("400x240")
app.title("Student Hello World")

# 3. Add a Modern Label

label = ctk.CTkLabel(master=app, text="Hello World!", font=("Roboto", 24))
label.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

# 4. Add a Button

button = ctk.CTkButton(master=app, text="Click Me", command=say_hello)
button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

# 5. Run the Application

app.mainloop()
Expected Output: A dark-themed window pops up with blue accents, a large "Hello World" heading, and a clickable button.

Common Issues & Fixes
Issue: ModuleNotFoundError: No module named 'customtkinter'.

Fix: I realized I was using a virtual environment but installed the package globally. I had to run pip install again inside my project's environment.

Issue: The window was too small to see the text.

Fix: Used app.geometry("400x240") to set a default starting size.

# References

CustomTkinter Documentation
Python Official Tutorialng-python-ai
