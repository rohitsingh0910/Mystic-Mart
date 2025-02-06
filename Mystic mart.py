import tkinter as tk
from tkinter import messagebox

class Mystic_Mart:
    def __init__(self, root):
        self.root = root
        self.root.title("Mystic Mart")
        self.stock = {}

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()

        # Create labels and entries
        self.label1 = tk.Label(self.frame1, text="Item Name:")
        self.label1.pack(side=tk.LEFT)
        self.entry1 = tk.Entry(self.frame1)
        self.entry1.pack(side=tk.LEFT)

        self.label2 = tk.Label(self.frame1, text="Quantity:")
        self.label2.pack(side=tk.LEFT)
        self.entry2 = tk.Entry(self.frame1)
        self.entry2.pack(side=tk.LEFT)

        # Create buttons
        self.button1 = tk.Button(self.frame2, text="Add Item", command=self.add_item)
        self.button1.pack(side=tk.LEFT)
        self.button2 = tk.Button(self.frame2, text="Remove Item", command=self.remove_item)
        self.button2.pack(side=tk.LEFT)
        self.button3 = tk.Button(self.frame2, text="Update Item", command=self.update_item)
        self.button3.pack(side=tk.LEFT)

        # Create listbox
        self.listbox = tk.Listbox(self.frame3)
        self.listbox.pack()

        self.load_data()

    def load_data(self):
        try:
            with open("stock_data.txt", "r") as f:
                for line in f.readlines():
                    item, quantity = line.strip().split(": ")
                    self.stock[item] = int(quantity)
                    self.listbox.insert(tk.END, f"{item}: {quantity}")
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("stock_data.txt", "w") as f:
            for item, quantity in self.stock.items():
                f.write(f"{item}: {quantity}\n")

    def add_item(self):
        item_name = self.entry1.get()
        try:
            quantity = int(self.entry2.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer")
            return

        if item_name and quantity:
            if item_name in self.stock:
                messagebox.showerror("Error", "Item already exists")
            else:
                self.stock[item_name] = quantity
                self.listbox.insert(tk.END, f"{item_name}: {quantity}")
                self.entry1.delete(0, tk.END)
                self.entry2.delete(0, tk.END)
                self.save_data()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def remove_item(self):
        item_name = self.entry1.get()
        if item_name:
            if item_name in self.stock:
                del self.stock[item_name]
                self.listbox.delete(0, tk.END)
                for item, quantity in self.stock.items():
                    self.listbox.insert(tk.END, f"{item}: {quantity}")
                self.entry1.delete(0, tk.END)
                self.entry2.delete(0, tk.END)
                self.save_data()
            else:
                messagebox.showerror("Error", "Item does not exist")
        else:
            messagebox.showerror("Error", "Please fill in item name")

    def update_item(self):
        item_name = self.entry1.get()
        try:
            quantity = int(self.entry2.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer")
            return

        if item_name and quantity:
            if item_name in self.stock:
                self.stock[item_name] = quantity
                self.listbox.delete(0, tk.END)
                for item, quantity in self.stock.items():
                    self.listbox.insert(tk.END, f"{item}: {quantity}")
                self.entry1.delete(0, tk.END)
                self.entry2.delete(0, tk.END)
                self.save_data()
            else:
                messagebox.showerror("Error", "Item does not exist")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

root = tk.Tk()
app = Mystic_Mart(root)
root.mainloop() 