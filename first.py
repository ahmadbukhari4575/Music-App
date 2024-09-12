import tkinter as tk

def on_click(event):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + event.widget.cget("text"))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget where expressions are inputted
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

# Create buttons and assign them to the grid
row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 18))
    btn.grid(row=row, column=col)
    if button == "C":
        btn.config(command=clear)
    elif button == "=":
        btn.config(command=calculate)
    else:
        btn.bind("<Button-1>", on_click)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter main loop
root.mainloop()
