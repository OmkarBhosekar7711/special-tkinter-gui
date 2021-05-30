import tkinter as tk
from tkinter import ttk
from EmployerTable import Table
from EmployerDetails import EmployerDetail

root = tk.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


notebook = ttk.Notebook(master=root)
# Given permission to expand inner element 
notebook.columnconfigure(0, weight=1) 
notebook.rowconfigure(0, weight=1)

# creating framing and inserting table and employer classes
Eframe = ttk.Frame(notebook)
Tframe = ttk.Frame(notebook)

# Given permission to table and form to expand 
Tframe.columnconfigure(0, weight=1)
Eframe.columnconfigure(0, weight=1)


employerFrame = EmployerDetail(Eframe)
tableFrame = Table(Tframe)

employerFrame.grid(padx=5, pady=5)
tableFrame.grid(padx=5, pady=5, sticky='swne')

notebook.add(Eframe, text='Employer Form')
notebook.add(Tframe, text='Employer Table')


notebook.grid(padx=5, pady=5, sticky='snwe')
root.title('Employer Dashboard')
root.mainloop()
