import tkinter as tk
from tkinter import ttk
from EmployerDatabase import Manager


class Table(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        data = Manager.load_data()

        tree = ttk.Treeview(master=parent, columns=(
            'Name', 
            'Surname', 
            'Aadhar', 
            'Phone Number', 
            'Category',
            'State'
        ), show ='headings')

        enumerated = enumerate(tree['columns'])

        for index, value in enumerated:  # index starts from 0
            tree.heading(index, text=value, anchor=tk.CENTER)  # indexing from 1 to 6

        for employee in data:
            tree.insert('', tk.END, values=employee,)

        def refresher():
            tree.delete(*tree.get_children())
            data = Manager.load_data()
            for employee in data:
                tree.insert('', tk.END, values=employee)

        tree.grid(padx=5, pady=5, sticky='swne')

        refres_btn = ttk.Button(master=parent, text='refresh to load', command=refresher).grid()
