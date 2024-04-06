from csv import writer
import tkinter
from tkinter import ttk


class GUI(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lab 10")
        self.geometry("240x220")
        self.resizable(False, False)

        self.user_input = []
        self.error_one = None

        self.name_label = tkinter.ttk.Label(self, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name = tkinter.StringVar(self)
        self.name_entry = tkinter.ttk.Entry(self, textvariable=self.name)
        self.name_entry.grid(row=0, column=1, columnspan=3)

        self.age_label = tkinter.Label(self, text="Age")
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.age = tkinter.StringVar(self)
        self.age_entry = tkinter.ttk.Entry(self, textvariable=self.age)
        self.age_entry.grid(row=1, column=1, columnspan=3)

        self.status_label = tkinter.Label(self, text="Status")
        self.status_label.grid(row=2, column=0, pady=10)
        self.status_selection = tkinter.StringVar()
        status_options = ["Student", "Staff", "Both"]
        for status in status_options:
            (tkinter.ttk.Radiobutton(text=status, variable=self.status_selection, value=status)
             .grid(row=2, column=status_options.index(status) + 1, pady=10))

        self.save = tkinter.ttk.Button(self, text="SAVE", command=self.refresh)
        self.save.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def refresh(self):
        if not self.get_age():
            self.error_one = tkinter.Label(self, text="Enter correct age value")
            self.error_one.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
        else:  # save & export vals
            self.user_input = [self.get_name(), self.get_age(), self.get_status()]
            self.export_csv()
            try:
                self.error_one.destroy()
            except AttributeError:
                pass  # ignore, if error DNE

        self.name_entry.delete(0, tkinter.END)
        self.age_entry.delete(0, tkinter.END)
        self.status_selection.set("nan")

    def get_name(self):
        if self.name.get() != "":
            return self.name.get().strip()
        else:
            return "Anonymous"

    def get_age(self):
        try:
            if int(self.age.get().strip()) > 0:
                return int(self.age.get().strip()) * 10
            else:
                raise ValueError
        except ValueError:
            return False

    def get_status(self):
        if self.status_selection.get() != "None":
            return self.status_selection.get().strip()
        else:
            return "NA"

    def get_user_input(self):
        return self.user_input

    def export_csv(self):
        with open("data.csv", 'a', newline='') as outbound_file:
            csv_writer = writer(outbound_file)
            csv_writer.writerow(self.get_user_input())
