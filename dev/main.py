import configparser
import tkinter as tk

config = configparser.ConfigParser()
config.read("../config.ini")

def on_button_click():
    label.config(text="Button clicked!")

root = tk.Tk()
root.title(config["Info"]["Name"])
root.geometry(config["Window"]["Size"])

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()