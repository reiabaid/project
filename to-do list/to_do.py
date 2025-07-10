import tkinter as tk
from tkinter import messagebox, filedialog

# --- Functions ---

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully.")

def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        task_listbox.delete(0, tk.END)
        with open(file_path, "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())

# --- GUI Setup ---

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.config(bg="#1e1e1e")

# Entry + Add Button
task_entry = tk.Entry(root, font=("Helvetica", 12), width=25)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

# Task List
task_listbox = tk.Listbox(root, width=40, height=15, font=("Courier", 10), selectbackground="#ffdd55")
task_listbox.pack(pady=10)

# Buttons: Delete, Save, Load
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

del_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
del_btn.grid(row=0, column=0, padx=5)

save_btn = tk.Button(btn_frame, text="Save Tasks", width=12, command=save_tasks)
save_btn.grid(row=0, column=1, padx=5)

load_btn = tk.Button(btn_frame, text="Load Tasks", width=12, command=load_tasks)
load_btn.grid(row=0, column=2, padx=5)

root.mainloop()
