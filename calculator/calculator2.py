import tkinter as tk

# 🎨 Color Theme
BG_COLOR = "#1e1e1e"
BTN_COLOR = "#333333"
BTN_TEXT = "#ffffff"
BTN_HIGHLIGHT = "#4ecca3"
DISPLAY_COLOR = "#282c34"
FONT = ('Consolas', 20)

# Create main window
window = tk.Tk()
window.title("Dark Mode Calculator")
window.geometry("320x460")
window.configure(bg=BG_COLOR)

# Entry widget (display)
entry = tk.Entry(window, font=FONT, bg=DISPLAY_COLOR, fg="#ffffff", borderwidth=0, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=20, sticky="nsew")

# Functions
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, font=FONT, bg=BTN_HIGHLIGHT, fg=BTN_TEXT,
                  activebackground="#5ff4c6", padx=20, pady=20,
                  command=calculate).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    elif text == 'C':
        tk.Button(window, text=text, font=FONT, bg="#ff5c5c", fg=BTN_TEXT,
                  activebackground="#ff8888", padx=20, pady=20,
                  command=clear).grid(row=row, column=col, columnspan=4, sticky="nsew", padx=5, pady=5)
    else:
        tk.Button(window, text=text, font=FONT, bg=BTN_COLOR, fg=BTN_TEXT,
                  activebackground="#505050", padx=20, pady=20,
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Grid configuration (make everything expand equally)
for i in range(6):
    window.rowconfigure(i, weight=1)
for j in range(4):
    window.columnconfigure(j, weight=1)

# Run the application
window.mainloop()

# This code creates a dark mode calculator GUI using Tkinter in Python.
# It includes buttons for digits, operations, and a clear function.
# The calculator evaluates expressions entered in the entry widget.
# The layout is managed using a grid system for better organization.
# The color theme is designed for a dark mode aesthetic.
