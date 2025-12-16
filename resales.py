import tkinter as tk
from tkinter import messagebox


# ---------------------------------
# RESALES WINDOW
# ---------------------------------
def open_resales(parent):

   import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# MAIN WINDOW
# -------------------------------
root = tk.Tk()
root.title("Digital Realtor")
root.geometry("800x700")
root.resizable(False, False)

# -------------------------------
# TITLE
# -------------------------------
tk.Label(root, text="Digital Realtor", font=("Arial", 24, "bold")).pack(pady=10)
tk.Label(root, text="Manage Client, House, and Agent Data", font=("Arial", 12)).pack(pady=5)

# -------------------------------
# CREATE NOTEBOOK (TABS)
# -------------------------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# -------------------------------
# CLIENT DATA TAB
# -------------------------------
client_frame = tk.Frame(notebook)
notebook.add(client_frame, text="Client Data")

tk.Label(client_frame, text="Client Name:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
client_name = tk.Entry(client_frame, width=40)
client_name.grid(row=0, column=1, pady=5)

tk.Label(client_frame, text="Phone Number:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
client_phone = tk.Entry(client_frame, width=40)
client_phone.grid(row=1, column=1, pady=5)

tk.Label(client_frame, text="Email Address:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
client_email = tk.Entry(client_frame, width=40)
client_email.grid(row=2, column=1, pady=5)

def save_client():
    messagebox.showinfo("Saved", f"Client '{client_name.get()}' saved successfully!")
    print("Client Data:")
    print("Name:", client_name.get())
    print("Phone:", client_phone.get())
    print("Email:", client_email.get())

tk.Button(client_frame, text="Save Client", command=save_client).grid(row=3, column=0, columnspan=2, pady=10)

# -------------------------------
# HOUSE DATA TAB
# -------------------------------
house_frame = tk.Frame(notebook)
notebook.add(house_frame, text="House Data")

# Scrollable Frame for House Tab
house_canvas = tk.Canvas(house_frame)
house_scrollbar = ttk.Scrollbar(house_frame, orient="vertical", command=house_canvas.yview)
house_scroll_frame = tk.Frame(house_canvas)

house_scroll_frame.bind(
    "<Configure>",
    lambda e: house_canvas.configure(scrollregion=house_canvas.bbox("all"))
)

house_canvas.create_window((0, 0), window=house_scroll_frame, anchor="nw")
house_canvas.configure(yscrollcommand=house_scrollbar.set)

house_canvas.pack(side="left", fill="both", expand=True)
house_scrollbar.pack(side="right", fill="y")

# -------------------------------
# HOUSE FORM FIELDS
# -------------------------------
fields = {}

def add_label_entry(parent, text, width=40):
    tk.Label(parent, text=text).pack(anchor="w", pady=2)
    entry = tk.Entry(parent, width=width)
    entry.pack(anchor="w", pady=2)
    return entry

def add_label_text(parent, text, width=50, height=4):
    tk.Label(parent, text=text).pack(anchor="w", pady=2)
    text_box = tk.Text(parent, width=width, height=height)
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
    chk = tk.Checkbutton(parent, text=text, variable=var)
    chk.pack(anchor="w", pady=2)
    return var

# Basic Property Info
fields['Property Type'] = add_label_entry(house_scroll_frame, "Property Type")
fields['Address'] = add_label_entry(house_scroll_frame, "Address")
fields['MLS / Listing ID'] = add_label_entry(house_scroll_frame, "MLS / Listing ID")
fields['Year Built'] = add_label_entry(house_scroll_frame, "Year Built")
fields['Lot Size / Acreage'] = add_label_entry(house_scroll_frame, "Lot Size / Acreage")
fields['Square Footage'] = add_label_entry(house_scroll_frame, "Square Footage")
fields['Bedrooms'] = add_label_entry(house_scroll_frame, "Bedrooms")
fields['Bathrooms'] = add_label_entry(house_scroll_frame, "Bathrooms")
fields['Floors / Levels'] = add_label_entry(house_scroll_frame, "Number of Floors / Levels")

# Interior Features
fields['Flooring Type'] = add_label_combobox(house_scroll_frame, "Flooring Type", ["Hardwood", "Carpet", "Tile", "Other"])
fields['Heating System'] = add_label_combobox(house_scroll_frame, "Heating System", ["Central", "Electric", "Gas", "Other"])
fields['Air Conditioning'] = add_label_combobox(house_scroll_frame, "Air Conditioning", ["Central", "Window Unit", "None"])
fields['Fireplace'] = add_label_checkbutton(house_scroll_frame, "Fireplace(s)")
fields['Kitchen Features'] = add_label_text(house_scroll_frame, "Kitchen Features")
fields['Laundry Room'] = add_label_checkbutton(house_scroll_frame, "Laundry Room")
fields['Basement'] = add_label_combobox(house_scroll_frame, "Basement", ["Finished", "Unfinished", "None"])

# Exterior Features
fields['Roof Type / Age'] = add_label_entry(house_scroll_frame, "Roof Type / Age")
fields['Garage'] = add_label_entry(house_scroll_frame, "Garage (Attached/Detached, # of cars)")
fields['Driveway Type'] = add_label_entry(house_scroll_frame, "Driveway Type")
fields['Yard / Landscaping'] = add_label_text(house_scroll_frame, "Yard / Landscaping")
fields['Pool / Hot Tub'] = add_label_checkbutton(house_scroll_frame, "Pool / Hot Tub")
fields['Deck / Patio / Balcony'] = add_label_checkbutton(house_scroll_frame, "Deck / Patio / Balcony")
fields['Fencing'] = add_label_entry(house_scroll_frame, "Fencing")

# Utilities & Systems
fields['Water Supply'] = add_label_combobox(house_scroll_frame, "Water Supply", ["Public", "Well"])
fields['Sewer / Septic'] = add_label_combobox(house_scroll_frame, "Sewer / Septic", ["Public", "Septic"])
fields['Electricity'] = add_label_checkbutton(house_scroll_frame, "Electricity")
fields['Gas'] = add_label_checkbutton(house_scroll_frame, "Gas")
fields['Internet / Cable'] = add_label_checkbutton(house_scroll_frame, "Internet / Cable")

# Community & Location
fields['School District'] = add_label_entry(house_scroll_frame, "School District")
fields['Neighborhood / HOA'] = add_label_entry(house_scroll_frame, "Neighborhood / HOA")
fields['Walkability / Nearby Amenities'] = add_label_text(house_scroll_frame, "Walkability / Nearby Amenities")
fields['Public Transportation'] = add_label_text(house_scroll_frame, "Public Transportation")
fields['Crime / Safety Rating'] = add_label_entry(house_scroll_frame, "Crime / Safety Rating")

# Financial & Legal Info
fields['Asking Price'] = add_label_entry(house_scroll_frame, "Asking Price")
fields['Property Tax'] = add_label_entry(house_scroll_frame, "Property Tax")
fields['HOA Fees'] = add_label_entry(house_scroll_frame, "HOA Fees")
fields['Zoning Type'] = add_label_entry(house_scroll_frame, "Zoning Type")
fields['Disclosure Statements'] = add_label_text(house_scroll_frame, "Disclosure Statements")
fields['Special Assessments'] = add_label_text(house_scroll_frame, "Special Assessments")

def save_house():
    data = {}
    for k, v in fields.items():
        if isinstance(v, tk.Entry):
            data[k] = v.get()
        elif isinstance(v, tk.Text):
            data[k] = v.get("1.0", tk.END).strip()
        elif isinstance(v, ttk.Combobox):
            data[k] = v.get()
        elif isinstance(v, tk.BooleanVar):
            data[k] = v.get()
    messagebox.showinfo("Saved", "House data saved successfully!")
    print("HOUSE DATA:")
    for key, val in data.items():
        print(f"{key}: {val}")

tk.Button(house_scroll_frame, text="Save House", command=save_house).pack(pady=10)

# -------------------------------
# AGENT PROCESS TAB (scrollable)
# -------------------------------
agent_frame = tk.Frame(notebook)
notebook.add(agent_frame, text="Agent Process")

# Scrollable Frame for Agent Tab
agent_canvas = tk.Canvas(agent_frame)
agent_scrollbar = ttk.Scrollbar(agent_frame, orient="vertical", command=agent_canvas.yview)
agent_scroll_frame = tk.Frame(agent_canvas)

agent_scroll_frame.bind(
    "<Configure>",
    lambda e: agent_canvas.configure(scrollregion=agent_canvas.bbox("all"))
)

agent_canvas.create_window((0, 0), window=agent_scroll_frame, anchor="nw")
agent_canvas.configure(yscrollcommand=agent_scrollbar.set)

agent_canvas.pack(side="left", fill="both", expand=True)
agent_scrollbar.pack(side="right", fill="y")

tk.Label(agent_scroll_frame, text="Transactions:", font=("Arial", 12, "bold")).pack(pady=5)
transactions_list = tk.Listbox(agent_scroll_frame, height=5)
transactions_list.pack(pady=5)

tk.Label(agent_scroll_frame, text="Assign Tasks", font=("Arial", 14, "bold")).pack(pady=5)

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

task_status = []

# Header
header_frame = tk.Frame(agent_scroll_frame)
header_frame.pack(pady=2, fill="x")
tk.Label(header_frame, text="Task", width=50, anchor="w", font=("Arial", 10, "bold")).pack(side="left", padx=5)
tk.Label(header_frame, text="Status", width=15, anchor="w", font=("Arial", 10, "bold")).pack(side="left", padx=5)

# Tasks with dropdowns
for task in tasks:
    row_frame = tk.Frame(agent_scroll_frame)
    row_frame.pack(fill="x", padx=5, pady=2)

    tk.Label(row_frame, text=task, width=50, anchor="w").pack(side="left")
    status = ttk.Combobox(row_frame, values=["Not Completed", "Completed"], width=12)
    status.current(0)
    status.pack(side="left", padx=5)
    task_status.append(status)

def save_transaction():
    results = "\n".join(f"{task}: {status.get()}" for task, status in zip(tasks, task_status))
    messagebox.showinfo("Saved", f"Transaction saved!\n\nTasks:\n{results}")
    print("Tasks:\n", results)

tk.Button(agent_scroll_frame, text="Save Transaction", command=save_transaction).pack(pady=10)

# -------------------------------
# RUN APP
# -------------------------------
root.mainloop()
