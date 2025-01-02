import tkinter as tk
from tkinter import *
import psutil

def update_ram_info():
    ram_info = psutil.virtual_memory()
    total_label.config(text=f"Total: {ram_info.total / 1024 / 1024 / 1024:.2f} GB")
    available_label.config(text=f"Available: {ram_info.available / 1024 / 1024 / 1024:.2f} GB")
    used_label.config(text=f"Used: {ram_info.used / 1024 / 1024 / 1024:.2f} GB")
    percentage_label.config(text=f"Percentage usage: {ram_info.percent}%")
    window.after(100, update_ram_info)
def main_window():
    global window
    global total_label, available_label, used_label, percentage_label

    window = tk.Tk()
    window.geometry("250x120")
    window.title("RAM Usage Viewer")
    window.geometry(f"+{(window.winfo_screenwidth() - 200) // 2}+{(window.winfo_screenheight() - 200) // 2}")
    window.configure(background="white")
    total_label = tk.Label(window, text="", background="white", font="Arial 15", fg="black")
    total_label.pack()
    available_label = tk.Label(window, text="", background="white", font="Arial 15", fg="black")
    available_label.pack()
    used_label = tk.Label(window, text="", background="white", font="Arial 15", fg="black")
    used_label.pack()
    percentage_label = tk.Label(window, text="", background="white", font="Arial 15", fg="black")
    percentage_label.pack()
    update_ram_info()
    window.mainloop()
if __name__ == '__main__':
    main_window()
