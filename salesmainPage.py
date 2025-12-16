# salesmainPage.py
import tkinter as tk
from tkinter import messagebox

def open_sales_main(parent):
    """
    Opens the Sales Main Page window.
    """
    window = tk.Toplevel(parent)
    window.title("Sales Main Page")
    window.geometry("500x550")
    window.resizable(False, False)

    tk.Label(window, text="Sales Main Page", font=("Arial", 20, "bold")).pack(pady=20)
    tk.Label(window, text="This is the sales main page.", font=("Arial", 12)).pack(pady=10)

    tk.Label(window, text="Transaction Name:", font=("Arial", 12)).pack(pady=5)
    entry_name = tk.Entry(window, width=40)
    entry_name.pack(pady=5)

    def save_transaction():
        name = entry_name.get().strip()
        if name:
            messagebox.showinfo("Saved", f"Transaction '{name}' saved successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a transaction name!")

    tk.Button(window, text="Save Transaction", width=20, bg="#88ccff", command=save_transaction).pack(pady=15)

    # Example buttons for future CRUD operations
    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=20)

    tk.Button(btn_frame, text="Create", width=20, bg="#88ccff",
              command=lambda: messagebox.showinfo("Create", "Create clicked!")).pack(pady=5)
    tk.Button(btn_frame, text="Edit", width=20, bg="#88ccff",
              command=lambda: messagebox.showinfo("Edit", "Edit clicked!")).pack(pady=5)
    tk.Button(btn_frame, text="Delete", width=20, bg="#88ccff",
              command=lambda: messagebox.showinfo("Delete", "Delete clicked!")).pack(pady=5)
    tk.Button(btn_frame, text="Search", width=20, bg="#88ccff",
              command=lambda: messagebox.showinfo("Search", "Search clicked!")).pack(pady=5)
