import tkinter as tk
from tkinter import *
import psutil
import time
def main_window():
    global window
    ram_info = psutil.virtual_memory()
    # Create the main window
    window = tk.Tk()
    window.geometry("300x200")
    window.title("RAM Usage Viewer")
    window.geometry(f"+{(window.winfo_screenwidth() - 200) // 2}+{(window.winfo_screenheight() - 200) // 2}")
    window.configure(background="white")


    label = tk.Label(window, text=(f"Total: {ram_info.total / 1024 / 1024 / 1024:.2f} GB"), background="white", font="Arial 15", fg="black")
    label.pack()
    label = tk.Label(window, text=(f"Available: {ram_info.available / 1024 / 1024 / 1024:.2f} GB"), background="white", font="Arial 15", fg="black")
    label.pack()
    label = tk.Label(window, text=(f"Used: {ram_info.used / 1024 / 1024 / 1024:.2f} GB"), background="white", font="Arial 15", fg="black")
    label.pack()
    label = tk.Label(window, text=(f"Percentage usage: {ram_info.percent}%"), background="white", font="Arial 15", fg="black")
    label.pack()

    button = tk.Button(window, text="Refresh", command=refresh_window, background="red", font="Arial 15", fg="white")
    button.pack()


    # Run the application
    window.mainloop()
def refresh_window():
    time.sleep(0)
    window.destroy()
    main_window()

if __name__ == '__main__': #первично вызываем главное окно при включении программы
    main_window()
    


