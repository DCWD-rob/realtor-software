import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------
def add_label_entry(parent, text):
    tk.Label(parent, text=text).pack(anchor="w", pady=2)
    entry = tk.Entry(parent, width=40)
    entry.pack(anchor="w", pady=2)
    return entry

def add_label_text(parent, text):
    tk.Label(parent, text=text).pack(anchor="w", pady=2)
    text_box = tk.Text(parent, width=50, height=4)
    text_box.pack(anchor="w", pady=2)
    return text_box

def add_label_combobox(parent, text, values):
    tk.Label(parent, text=text).pack(anchor="w", pady=2)
    combo = ttk.Combobox(parent, values=values, state="readonly")
    combo.current(0)
    combo.pack(anchor="w", pady=2)
    return combo

def add_label_checkbutton(parent, text):
    var = tk.BooleanVar()
    tk.Checkbutton(parent, text=text, variable=var).pack(anchor="w", pady=2)
    return var

# -------------------------------
# CLIENT TAB
# -------------------------------
def create_client_tab(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Client Data")

    name = add_label_entry(frame, "Client Name")
    phone = add_label_entry(frame, "Phone Number")
    email = add_label_entry(frame, "Email Address")

    def save():
        messagebox.showinfo("Saved", f"Client {name.get()} saved")
        print(name.get(), phone.get(), email.get())

    tk.Button(frame, text="Save Client", command=save).pack(pady=10)

# -------------------------------
# HOUSE TAB
# -------------------------------
def create_house_tab(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="House Data")

    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll = tk.Frame(canvas)

    scroll.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    add_label_entry(scroll, "Property Type")
    add_label_entry(scroll, "Address")
    add_label_entry(scroll, "Bedrooms")
    add_label_entry(scroll, "Bathrooms")
    add_label_combobox(scroll, "Pool", ["In ground", "Above ground", "None"])
    add_label_checkbutton(scroll, "Fireplace")
    add_label_text(scroll, "Notes")

    tk.Button(scroll, text="Save House",
              command=lambda: messagebox.showinfo("Saved", "House saved")).pack(pady=10)

# -------------------------------
# AGENT TAB
# -------------------------------
def create_agent_tab(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Agent Process")

    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll = tk.Frame(canvas)

    scroll.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scroll, text="Assign Tasks", font=("Arial", 14, "bold")).pack(pady=5)

    tasks = [
        "mandatory licenses consumer",
        "MA-Exc buyers agency agreement",
        "TRID addendum",
        "lender approval",
        "deed",
        "MLS Listing",
        "contract to purchase Real estate",
        "offer deposit",
        "lead paint notice",
        "MA standard P and S agreement",
        "P and S deposit",
        "MA notice of designated agency",
        "facts for consumers",
        "sellers real estate info statement",
        "closing documents",
        "DA"
    ]
    statuses = []

    for task in tasks:
        row = tk.Frame(scroll)
        row.pack(fill="x", pady=2)
        tk.Label(row, text=task, width=40, anchor="w").pack(side="left")
        cb = ttk.Combobox(row, values=["Not Completed", "Completed"], width=15)
        cb.current(0)
        cb.pack(side="left")
        statuses.append(cb)

    def save():
        result = "\n".join(f"{t}: {s.get()}" for t, s in zip(tasks, statuses))
        messagebox.showinfo("Saved", result)
        print(result)

    tk.Button(scroll, text="Save Transaction", command=save).pack(pady=10)

# -------------------------------
# BUYING WINDOW
# -------------------------------
def open_buying_window(parent):
    window = tk.Toplevel(parent)
    window.title("Buying Transactions")
    window.geometry("800x700")

    notebook = ttk.Notebook(window)
    notebook.pack(expand=True, fill="both", padx=10, pady=10)

    create_client_tab(notebook)
    create_house_tab(notebook)
    create_agent_tab(notebook)

# -------------------------------
# MAIN APP
# -------------------------------
def main():
    root = tk.Tk()
    root.title("Main App")
    root.geometry("300x200")

    tk.Button(root, text="Open Buying Window",
              command=lambda: open_buying_window(root)).pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
