import tkinter as tk
import subprocess

def say_hello():
    label.config(text="Hello, World!", font=("Arial", 20, "bold"), bg="light blue", fg="white")

def say_goodbye():
    label.config(text="Goodbye, World!", font=("Arial", 20, "bold"), bg="red", fg="white")
    count_down(5)

def count_down(time):
    if time > 0:
        label.config(text=str(time))
        root.after(1000, count_down, time-1)
    else:
        root.destroy()

def open_drawio():
    subprocess.run(["C:\Program Files\Draw.io\draw.io.exe"])

root = tk.Tk()
root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Hello World")
root.configure(bg="light gray")

button1 = tk.Button(root, text="Press me", command=say_hello, font=("Arial", 20, "bold"), bg="green", fg="white")
button1.pack(side="left", padx=50)

button2 = tk.Button(root, text="Open Draw.io", command=open_drawio, font=("Arial", 20, "bold"), bg="purple", fg="white")
button2.pack(side="left", padx=50)

button3 = tk.Button(root, text="Goodbye World", command=say_goodbye, font=("Arial", 20, "bold"), bg="red", fg="white")
button3.pack(side="top", padx=50, pady=50, anchor='ne')

label = tk.Label(root, font=("Arial", 20, "bold"), bg="white", fg="black")
label.pack(pady=50)

root.mainloop()
