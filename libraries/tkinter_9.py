import tkinter as tk

root = tk.Tk()
root.title("Simple App")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me", command=lambda: label.config(text="You Clicked!"))
button.pack()

root.mainloop()
