import tkinter as tk
from tkinter import simpledialog, messagebox

class MultiListToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabbed To-Do List")
        self.root.geometry("500x600")
        self.root.configure(bg="#ffe6f0")

        self.lists = {}  # Dictionary to store multiple lists
        self.current_list = None

        # --- Title + New List ---
        top_frame = tk.Frame(self.root, bg="#ffe6f0")
        top_frame.pack(pady=10)

        self.list_title = tk.Label(top_frame, text="", font=("Courier New", 14, "bold"), bg="#ffe6f0", fg="#333")
        self.list_title.pack(side="left", padx=10)

        self.new_list_btn = tk.Button(top_frame, text="➕ New List", command=self.create_new_list,
                                      bg="#ff99cc", font=("Courier New", 10, "bold"))
        self.new_list_btn.pack(side="right", padx=10)

        # --- List Selector ---
        self.tab_frame = tk.Frame(self.root, bg="#ffe6f0")
        self.tab_frame.pack(pady=5)

        # --- Task Entry ---
        self.task_entry = tk.Entry(self.root, font=("Courier New", 12), width=30, bg="white")
        self.task_entry.pack(pady=6)

        self.add_btn = tk.Button(self.root, text="Add Task", command=self.add_task,
                                 bg="#ff99cc", font=("Courier New", 10, "bold"))
        self.add_btn.pack(pady=5)

        # --- Tasks Display ---
        self.task_canvas = tk.Canvas(self.root, bg="#ffe6f0", highlightthickness=0, width=430, height=350)
        self.task_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.task_canvas.yview)
        self.task_frame = tk.Frame(self.task_canvas, bg="#ffe6f0")

        self.task_frame.bind("<Configure>", lambda e: self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all")))
        self.task_canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.task_canvas.configure(yscrollcommand=self.task_scrollbar.set)

        self.task_canvas.pack(side="left", fill="both", expand=True, padx=(30, 0), pady=10)
        self.task_scrollbar.pack(side="right", fill="y", padx=(0, 20))

        # --- Buttons ---
        self.btn_frame = tk.Frame(self.root, bg="#ffe6f0")
        self.btn_frame.pack(pady=5)

        self.delete_btn = tk.Button(self.btn_frame, text="Delete Selected", command=self.delete_selected_tasks,
                                    bg="#ff99cc", font=("Courier New", 10, "bold"), width=16)
        self.delete_btn.grid(row=0, column=0, padx=5)

        self.create_new_list("My List")  # Create a default list

    def create_new_list(self, name=None):
        if not name:
            name = simpledialog.askstring("New List", "Enter list name:")
            if not name:
                return

        if name in self.lists:
            messagebox.showinfo("Exists", "A list with this name already exists.")
            return

        self.lists[name] = []
        self.add_tab(name)
        self.switch_list(name)

    def add_tab(self, name):
        btn = tk.Button(self.tab_frame, text=name, command=lambda n=name: self.switch_list(n),
                        bg="#ffccdd", font=("Courier New", 9, "bold"), width=10)
        btn.pack(side="left", padx=4)

    def switch_list(self, name):
        self.current_list = name
        self.list_title.config(text=name)

        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task_text, var in self.lists[name]:
            cb = tk.Checkbutton(self.task_frame, text=task_text, variable=var,
                                font=("Courier New", 11, "bold"), bg="#ffe6f0",
                                activebackground="#ffe6f0", selectcolor="#ffe6f0",
                                anchor="w", wraplength=300)
            cb.var = var
            cb.pack(fill="x", pady=4, padx=5, anchor="w")

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text or not self.current_list:
            return

        var = tk.BooleanVar()
        cb = tk.Checkbutton(self.task_frame, text=task_text, variable=var,
                            font=("Courier New", 11, "bold"), bg="#ffe6f0",
                            activebackground="#ffe6f0", selectcolor="#ffe6f0",
                            anchor="w", wraplength=300)
        cb.var = var
        cb.pack(fill="x", pady=4, padx=5, anchor="w")

        self.lists[self.current_list].append((task_text, var))
        self.task_entry.delete(0, tk.END)

    def delete_selected_tasks(self):
        if not self.current_list:
            return

        new_task_list = []
        for widget in self.task_frame.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                if not widget.var.get():
                    new_task_list.append((widget.cget("text"), widget.var))
                else:
                    widget.destroy()
        self.lists[self.current_list] = new_task_list


# --- RUN APP ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiListToDoApp(root)
    root.mainloop()
# This code implements a multi-list to-do application using Tkinter.
# It allows users to create multiple lists, add tasks to each list, and delete selected tasks