import tkinter as tk
from tkinter import ttk
from EmployerDatabase import Manager
import pycountry


class EmployerDetail(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        employerBorder = tk.LabelFrame(master = parent, text='EmployerDetail')
        employerBorder.grid(padx=5, pady=5, sticky='snwe')

        nameVar = tk.StringVar()
        employerName = ttk.Label(master=employerBorder, text='Name').grid(padx=5, pady=5, row=0,)
        employernameInputBox = ttk.Entry(master=employerBorder, textvariable=nameVar).grid(padx=5, pady=5, column=1, row=0)

        surnameVar = tk.StringVar()
        employerSurname = ttk.Label(master=employerBorder, text='Surname').grid(padx=5, pady=5, row=2)
        employerSurnameInputBox = ttk.Entry(master=employerBorder, textvariable=surnameVar).grid(padx=5, pady=5, column=1, row=2)

        addharVar = tk.StringVar()
        employerAadhar = ttk.Label(master=employerBorder, text='Aadhar Number').grid(padx=5, pady=5, row=3)
        employerAadharInputBox = ttk.Entry(master=employerBorder, textvariable=addharVar).grid(padx=5, pady=5, column=1, row=3)

        phoneVar = tk.StringVar()
        employerPhone = ttk.Label(master=employerBorder, text='Phone Number').grid(padx=5, pady=5, row=4)
        employerPhoneInputBox = ttk.Entry(master=employerBorder, textvariable=phoneVar).grid(padx=5, pady=5, column=1, row=4)

        employerdeparment = ttk.Label(master=employerBorder, text='Select Category').grid(padx=5, pady=5, row=5)
        employerdeparmentComboVar = tk.StringVar()
        employerdeparmentCombo = ttk.Combobox(master=employerBorder, text='Select Category: ', value=[
            'Product Management',
            'Shipping Management', 
            'Network Management', 
            'Product Designer', 
            'Software Dev', 
            'Hardware Dev', 
        ], textvariable=employerdeparmentComboVar).grid(padx=5, pady=5, row=5, column=1)

        stateLabel = ttk.Label(master=employerBorder, text='Select state').grid(padx=5, pady=5, row=6, column=0)
        StateVar = tk.StringVar()
        employerState = ttk.Combobox(master=employerBorder, textvariable=StateVar, value=[state.name for state in pycountry.subdivisions.lookup('in')])
        employerState.grid(padx=5, pady=5, row=6, column=1)

        def collect_data():
            # employernameInputBox.delete(0, 'end')
            # employerSurnameInputBox.delete(0, 'end')
            # employerPhoneInputBox.delete(0, 'end')
            # employerAadharInputBox.delete(0, 'end')
            # employerdeparmentCombo.delete(0, 'end')
            # employerState.delete(0, 'end')

            Manager.add_value(value=(
                nameVar.get(), 
                surnameVar.get(), 
                addharVar.get(), 
                phoneVar.get(), 
                employerdeparmentComboVar.get(),
                StateVar.get()
            ))

            Manager.load_data()

        submitBtn = ttk.Button(master=employerBorder, text='Submit', command=collect_data)
        submitBtn.grid(padx=5, pady=5)
