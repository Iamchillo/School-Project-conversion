Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
from tkinter import ttk
from funcs import *  

# Mapping of functions for conversion
conversion_functions = {
    ('decimal', 'binary'): decimal_to_binary, 
    ('decimal', 'octal'): decimal_to_octal,
    ('decimal', 'hexadecimal'): decimal_to_hex, 
    ('binary', 'decimal'): binary_to_decimal, 
    ('binary', 'octal'): binary_to_octal, 
    ('binary', 'hexadecimal'): binary_to_hex, 
    ('octal', 'decimal'): octal_to_decimal, 
    ('octal', 'binary'): octal_to_binary, 
    ('octal', 'hexadecimal'): octal_to_hexa, 
    ('hexadecimal', 'decimal'): hexa_to_decimal, 
    ('hexadecimal', 'binary'): hexa_to_binary, 
    ('hexadecimal', 'octal'): hexa_to_octal 
}

allowed = ['decimal', 'hexadecimal', 'binary', 'octal']

# Function to perform conversion
def convert(number, v_from, v_to):
    try:
        if not number:
            return "A number is required."
        if v_from not in allowed:
            return "Invalid input"
        if v_to not in allowed:
            return "Invalid output"
        if v_from == v_to:
            return "Both bases cannot be equal"
        conversion_func = conversion_functions.get((v_from, v_to))

        if v_from == "decimal":
            number = int(number)
        else:
            number = str(number)

        converted = conversion_func(number)
        return converted
    except Exception as e:
        return f"{e}"

# Function to update the result in the GUI
def perform_conversion():
    number = entry_number.get()
    v_from = combo_from.get().lower()
    v_to = combo_to.get().lower()
    result = convert(number, v_from, v_to)
    label_result.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Number Base Converter")
root.geometry("400x300")

# Input Number
label_number = tk.Label(root, text="Enter the number:")
label_number.pack(pady=5)
entry_number = tk.Entry(root, width=30)
entry_number.pack(pady=5)

# Base to convert from
label_from = tk.Label(root, text="Convert from:")
label_from.pack(pady=5)
combo_from = ttk.Combobox(root, values=allowed, state="readonly")
combo_from.current(0)  # Set default selection
combo_from.pack(pady=5)

# Base to convert to
label_to = tk.Label(root, text="Convert to:")
label_to.pack(pady=5)
combo_to = ttk.Combobox(root, values=allowed, state="readonly")
combo_to.current(1)  # Set default selection
combo_to.pack(pady=5)

# Convert Button
button_convert = tk.Button(root, text="Convert", command="perform_conversion")
button_convert.pack(pady=10)

# Label to show the result
label_result = tk.Label(root, text="Result:")
label_result.pack(pady=10)


# Run the application
root.mainloop()
