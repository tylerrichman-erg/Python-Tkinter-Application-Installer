import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

# Create main window
root = tk.Tk()
root.title("Basic Tkinter App")
root.geometry("300x200")  # width x height

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Run the application
root.mainloop()