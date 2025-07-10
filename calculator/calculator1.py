import tkinter as tk

# Main window
window = tk.Tk()
window.title("Calculator")
window.geometry("320x500")

# Entry widget
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=4, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

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

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=calculate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(window, text=text, padx=138, pady=20, font=('Arial', 14),
                  command=clear).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Run the app
window.mainloop()
# This code creates a simple calculator GUI using Tkinter in Python.
# It includes buttons for digits, operations, and a clear function.
# The calculator evaluates expressions entered in the entry widget.
# The layout is managed using a grid system for better organization.