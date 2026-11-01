import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Registration Page")
root.geometry("450x650")

# Heading
tk.Label(root, text="Registration Page",
         font=("Arial", 18, "bold")).pack(pady=10)

# First Name
tk.Label(root, text="First Name").pack()
first = tk.Entry(root)
first.pack()

# Middle Name
tk.Label(root, text="Middle Name").pack()
middle = tk.Entry(root)
middle.pack()

# Last Name
tk.Label(root, text="Last Name").pack()
last = tk.Entry(root)
last.pack()

# Country Code
tk.Label(root, text="Country Code").pack()
country = ttk.Combobox(root, values=[
    "+91 India", "+1 USA", "+44 UK",
    "+61 Australia", "+971 UAE"
], state="readonly")
country.current(0)
country.pack()

# Mobile Number
tk.Label(root, text="Mobile Number").pack()
mobile = tk.Entry(root)
mobile.pack()

# State
tk.Label(root, text="State").pack()
state = ttk.Combobox(root, values=[
    "Andhra Pradesh", "Arunachal Pradesh", "Assam",
    "Bihar", "Chhattisgarh", "Goa", "Gujarat",
    "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh",
    "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal"
], state="readonly")
state.pack()

# District
tk.Label(root, text="District").pack()
district = ttk.Combobox(root, values=[
    "Kolhapur", "Pune", "Mumbai", "Sangli", "Satara"
], state="readonly")
district.pack()

# Taluka
tk.Label(root, text="Taluka").pack()
taluka = ttk.Combobox(root, values=[
    "Karvir", "Kagal","Hatkanangale", "Shirol",
    "Haveli", "Shirur"
], state="readonly")
taluka.pack()

# Address
tk.Label(root, text="Address").pack()
address = tk.Text(root, height=3, width=30)
address.pack()


# Submit Function
def submit():
    fname = first.get().strip()
    mname = middle.get().strip()
    lname = last.get().strip()
    phone = mobile.get().strip()
    addr = address.get("1.0", tk.END).strip()

    if not fname.isalpha() or not lname.isalpha():
        messagebox.showerror("Error", "Enter valid first and last names")

    elif mname and not mname.isalpha():
        messagebox.showerror("Error", "Enter a valid middle name")

    elif len(phone) != 10 or not phone.isdigit():
        messagebox.showerror("Error", "Enter a 10-digit mobile number")

    elif not state.get() or not district.get() or not taluka.get():
        messagebox.showerror("Error", "Select state, district and taluka")

    elif len(addr) < 5:
        messagebox.showerror("Error", "Enter a valid address")

    else:
        messagebox.showinfo(
            "Success",
            "Registration Successful!\n\n"
            f"Name: {fname} {mname} {lname}\n"
            f"Country Code: {country.get()}\n"
            f"Mobile: {phone}\n"
            f"State: {state.get()}\n"
            f"District: {district.get()}\n"
            f"Taluka: {taluka.get()}\n"
            f"Address: {addr}"
        )


# Submit Button
tk.Button(root, text="Submit", command=submit,
          bg="green", fg="white",
          font=("Arial", 12)).pack(pady=15)

root.mainloop()