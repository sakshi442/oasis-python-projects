import tkinter as tk
from tkinter import messagebox

# ----------------- CALCULATION ----------------- #
def calculate():
    try:
        # Get user input
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return

    # Convert units
    if weight_unit.get() == "lbs":
        weight *= 0.453592
    if height_unit.get() == "feet":
        height *= 0.3048

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Display results
    result_label.config(text=f"BMI: {bmi:.2f} ({category})")

# ----------------- GUI ----------------- #
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x250")

# Weight input
tk.Label(root, text="Weight:").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()
weight_unit = tk.StringVar(value="kgs")
tk.OptionMenu(root, weight_unit, "kgs", "lbs").pack()

# Height input
tk.Label(root, text="Height:").pack()
height_entry = tk.Entry(root)
height_entry.pack()
height_unit = tk.StringVar(value="meters")
tk.OptionMenu(root, height_unit, "meters", "feet").pack()

# Calculate button
tk.Button(root, text="Calculate BMI", command=calculate).pack(pady=10)

# Result
result_label = tk.Label(root, text="BMI: ")
result_label.pack()

root.mainloop()