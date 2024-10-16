import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def nether_portal_calculator(overworld_x, overworld_z, direction):
    nether_ratio = 8  

    if direction == "to_nether":
        nether_x = overworld_x / nether_ratio
        nether_z = overworld_z / nether_ratio
        return f"Nether Coordinates: X: {nether_x:.2f}, Z: {nether_z:.2f}"

    elif direction == "to_overworld":
        overworld_x = overworld_x * nether_ratio
        overworld_z = overworld_z * nether_ratio
        return f"Overworld Coordinates: X: {overworld_x:.2f}, Z: {overworld_z:.2f}"
    
    else:
        return "Invalid direction. Please choose 'to_nether' or 'to_overworld'."

def calculate_coordinates():
    try:
        overworld_x = float(x_entry.get())
        overworld_z = float(z_entry.get())
        direction = direction_var.get()

        result = nether_portal_calculator(overworld_x, overworld_z, direction)
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric coordinates.")

root = tk.Tk()
root.title("Nether Portal Calculator")

window_width, window_height = 350, 400  
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

style = ttk.Style()
style.theme_use('clam')

style.configure('TLabel', font=('Helvetica', 10), background="#2c3e50", foreground="white")
style.configure('TButton', font=('Helvetica', 10), padding=6, background="#34495e", foreground="white")
style.configure('TEntry', font=('Helvetica', 10), padding=4)
style.configure('TFrame', background="#2c3e50")
style.map('TButton', background=[('active', '#2980b9')], foreground=[('active', 'white')])

main_frame = ttk.Frame(root, padding="10 10 10 10") 
main_frame.pack(fill="both", expand=True)

title_label = ttk.Label(main_frame, text="Nether Portal Calculator", font=("Arial", 14, "bold"))
title_label.pack(pady=5)

direction_var = tk.StringVar(value="to_nether")
direction_label = ttk.Label(main_frame, text="Convert to:")
direction_label.pack(pady=(5, 0))

direction_frame = ttk.Frame(main_frame)
direction_frame.pack(pady=(5, 5))

to_nether_radio = ttk.Radiobutton(direction_frame, text="To Nether", variable=direction_var, value="to_nether")
to_nether_radio.pack(side="left", padx=5)

to_overworld_radio = ttk.Radiobutton(direction_frame, text="To Overworld", variable=direction_var, value="to_overworld")
to_overworld_radio.pack(side="right", padx=5)

# Coordinate input fields
x_label = ttk.Label(main_frame, text="Enter Overworld X coordinate:")
x_label.pack()

x_entry = ttk.Entry(main_frame, width=15)
x_entry.pack(pady=(5, 5))

z_label = ttk.Label(main_frame, text="Enter Overworld Z coordinate:")
z_label.pack()

z_entry = ttk.Entry(main_frame, width=15)
z_entry.pack(pady=(5, 5))

calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate_coordinates)
calculate_button.pack(pady=10)

result_label = ttk.Label(main_frame, text="", font=("Arial", 10))
result_label.pack(pady=5)

root.configure(bg="#2c3e50")

root.mainloop()
