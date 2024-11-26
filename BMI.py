import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# Database setup
def init_db():
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS bmi_records (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      weight REAL,
                      height REAL,
                      bmi REAL,
                      date TEXT)""")
    conn.commit()
    conn.close()

def save_data(name, weight, height, bmi):
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bmi_records (name, weight, height, bmi, date) VALUES (?, ?, ?, ?, ?)",
                   (name, weight, height, bmi, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        
        bmi = weight / (height ** 2)
        category = ""
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        save_data(name, weight, height, bmi)
        messagebox.showinfo("BMI Saved", "Your BMI record has been saved.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

tk.Label(root, text="Height (m):").grid(row=2, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1)

calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Your BMI will be displayed here.")
result_label.grid(row=4, column=0, columnspan=2)

# Initialize database and run GUI
init_db()
root.mainloop()
