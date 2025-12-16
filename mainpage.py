import tkinter as tk
from tkinter import messagebox
import RE_sales_main  # Import the separate RE_sales_main.py script
import REbuyermain  # Import the separate REbuyermain.py script
class DigitalRealtorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Realtor")
        self.root.geometry("500x550")

        # -------------------------------
        # TITLE
        # -------------------------------
        tk.Label(root, text="Digital Realtor", font=("Arial", 28, "bold")).pack(pady=25)
        tk.Label(root, text="Real Estate Transaction Manager").pack(pady=5)

        # -------------------------------
        # BUTTONS
        # -------------------------------
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Client Contact", width=30,
                  command=self.client_contact).pack(pady=6)
        tk.Button(btn_frame, text="Business Contact", width=30,
                  command=self.business_contact).pack(pady=6)
        tk.Button(btn_frame, text="Real Estate Transactions for selling", width=30,
                  command=self.realestate_transactions_selling).pack(pady=6)
        tk.Button(btn_frame, text="Real Estate Transactions for buying", width=30,
                  command=self.realestate_transactions_buying).pack(pady=6)
        tk.Button(btn_frame, text="Help", width=30,
                  command=self.help_info).pack(pady=6)
        tk.Button(btn_frame, text="Exit Program", width=30,
                  command=root.quit).pack(pady=6)

    # -------------------------------
    # CLIENT CONTACT WINDOW
    # -------------------------------
    def client_contact(self):
        window = tk.Toplevel(self.root)
        window.title("Client Contact")
        window.geometry("400x350")

        tk.Label(window, text="Client Contact", font=("Arial", 18, "bold")).pack(pady=10)

        form = tk.Frame(window)
        form.pack(pady=10)

        tk.Label(form, text="Client Name").grid(row=0, column=0, sticky="w")
        name_entry = tk.Entry(form, width=30)
        name_entry.grid(row=0, column=1)

        tk.Label(form, text="Phone Number").grid(row=1, column=0, sticky="w")
        phone_entry = tk.Entry(form, width=30)
        phone_entry.grid(row=1, column=1)

        tk.Label(form, text="Email Address").grid(row=2, column=0, sticky="w")
        email_entry = tk.Entry(form, width=30)
        email_entry.grid(row=2, column=1)

        tk.Label(form, text="Property Address").grid(row=3, column=0, sticky="w")
        address_entry = tk.Entry(form, width=30)
        address_entry.grid(row=3, column=1)

        def save_client():
            messagebox.showinfo(
                "Saved",
                f"Client '{name_entry.get()}' saved successfully!"
            )
            window.destroy()

        tk.Button(window, text="Save Client",
                  width=20, command=save_client).pack(pady=15)

    # -------------------------------
    # BUSINESS CONTACT WINDOW
    # -------------------------------
    def business_contact(self):
        window = tk.Toplevel(self.root)
        window.title("Business Contact")
        window.geometry("450x420")

        tk.Label(window, text="Business Contact", font=("Arial", 18, "bold")).pack(pady=10)

        form = tk.Frame(window)
        form.pack(pady=10)

        tk.Label(form, text="Company Name").grid(row=0, column=0, sticky="w")
        company_entry = tk.Entry(form, width=35)
        company_entry.grid(row=0, column=1)

        tk.Label(form, text="Address").grid(row=1, column=0, sticky="w")
        address_entry = tk.Entry(form, width=35)
        address_entry.grid(row=1, column=1)

        tk.Label(form, text="Phone Number").grid(row=2, column=0, sticky="w")
        phone_entry = tk.Entry(form, width=35)
        phone_entry.grid(row=2, column=1)

        tk.Label(form, text="Contact Name").grid(row=3, column=0, sticky="w")
        contact_entry = tk.Entry(form, width=35)
        contact_entry.grid(row=3, column=1)

        tk.Label(form, text="Email").grid(row=4, column=0, sticky="w")
        email_entry = tk.Entry(form, width=35)
        email_entry.grid(row=4, column=1)

        tk.Label(form, text="Notes").grid(row=5, column=0, sticky="nw")
        notes_box = tk.Text(form, width=35, height=5)
        notes_box.grid(row=5, column=1)

        def save_business():
            if company_entry.get() == "":
                messagebox.showerror("Error", "Company Name is required")
                return
            messagebox.showinfo(
                "Saved",
                f"Business '{company_entry.get()}' saved successfully!"
            )
            window.destroy()

        tk.Button(window, text="Save Business Contact",
                  width=25, command=save_business).pack(pady=15)

    # -------------------------------
    # REAL ESTATE TRANSACTIONS
    # -------------------------------
    def realestate_transactions_selling(self):
        # Open the separate RE_sales_main window
        RE_sales_main.open_sales_window(self.root)

    def realestate_transactions_buying(self):
        # Open the separate RE_sales_main window
        REbuyermain.open_buying_window(self.root)


    # -------------------------------
    # HELP
    # -------------------------------
    def help_info(self):
        messagebox.showinfo(
            "Help",
            "This program helps manage real estate clients and transactions."
        )

# -------------------------------
# START PROGRAM
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalRealtorApp(root)
    root.mainloop()
