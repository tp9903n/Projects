# Code by Benjamin Hawkins bh1625a

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Toplevel, StringVar
from tkinter.ttk import Combobox, Label, Button
from CandidateList import CandidateList, Candidate
from VoteCount import win_count


class CastVoteWindow(Toplevel):
    """Opens a new window that displays the positions voters can vote for"""

    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.title("Candidate Voting")
        self.geometry("400x400")

        # Prevent multiple Toplevel windows from being created
        self.focus_set()
        self.grab_set()

        self.pres_btn = Button(self, text="President", command=self.open_pres_win)
        self.pres_btn.grid(row=0, column=0)
        self.officer_btn = Button(self, text="GSU Officer", command=self.open_off_win)
        self.officer_btn.grid(row=1, column=0)
        self.flas_btn = Button(self, text="Faculty Officer for Arts and Sciences (FLAS)", command=self.open_flas_win)
        self.flas_btn.grid(row=2, column=0)
        self.bus_btn = Button(self, text="Faculty Officers for Business (BUS)", command=self.open_bus_win)
        self.bus_btn.grid(row=3, column=0)
        self.feh_btn = Button(self, text="Faculty Officers for Education and Health (FEH)", command=self.open_feh_win)
        self.feh_btn.grid(row=4, column=0)
        self.fes_btn = Button(self, text="Faculty Officers for Engineering and Science (FES)", command=self.open_fes_win)
        self.fes_btn.grid(row=5, column=0)

    # Open a new window and populate it with information from one of the new window subclasses
    def open_pres_win(self):
        self.pres_btn["state"] = "disabled"
        PresWindow(self)

    def open_off_win(self):
        self.officer_btn["state"] = "disabled"
        OffWindow(self)

    def open_flas_win(self):
        self.flas_btn["state"] = "disabled"
        FLASWindow(self)

    def open_bus_win(self):
        self.bus_btn["state"] = "disabled"
        BUSWindow(self)

    def open_feh_win(self):
        self.feh_btn["state"] = "disabled"
        FEHWindow(self)

    def open_fes_win(self):
        self.fes_btn["state"] = "disabled"
        FESWindow(self)


class NewWindow(Toplevel):
    """A generic window class that contains information relevant to all candidate positions"""



    def __init__(self, master):

        Toplevel.__init__(self, master)
        self.geometry("350x600")
        vote_label = Label(self, text="Please select your preferred candidate")
        vote_label.grid(row=0, column=0)
        # Prevent multiple Toplevel windows from being created
        self.focus_set()
        self.grab_set()

        first_preference = Label(self, text=" First Preference")
        first_preference.grid(row=1, column=0, pady=10)

        second_preference = Label(self, text=" Second Preference")
        second_preference.grid(row=3, column=0, pady=10)

        third_preference = Label(self, text=" Third Preference")
        third_preference.grid(row=5, column=0, pady=10)

        fourth_preference = Label(self, text=" Fourth Preference")
        fourth_preference.grid(row=7, column=0, pady=10)

        self.error_var = StringVar()
        self.error_var.set(" ")
        self.error_label = Label(self, textvariable=self.error_var)
        self.error_label.grid(row=9, column=0, pady=10)

        self.can_list = CandidateList.candidate_list
        self.can_names = []

        self.first_combo = Combobox(self, values=self.can_names)
        self.first_combo.grid(row=2, column=0)
        self.second_combo = Combobox(self, values=self.can_names)
        self.second_combo.grid(row=4, column=0)
        self.third_combo = Combobox(self, values=self.can_names)
        self.third_combo.grid(row=6, column=0)
        self.fourth_combo = Combobox(self, values=self.can_names)
        self.fourth_combo.grid(row=8, column=0)

        self.save_btn = Button(self, text="Save Votes", command=self.save_votes)
        self.save_btn.grid(row=10, column=1)

        self.can_position = ""

    def save_votes(self):
        """Checks votes have been correctly selected and saves the result to Votes.txt"""
        if self.first_combo.get() == "":
            self.error_var.set("You must select a first preference")
        elif (self.first_combo.get() != "") and self.first_combo.get() == self.second_combo.get() or \
                self.first_combo.get() == self.third_combo.get() or \
                self.first_combo.get() == self.fourth_combo.get() or \
                self.second_combo.get() == self.third_combo.get() or \
                self.second_combo.get() == self.fourth_combo.get() or \
                self.third_combo.get() == self.fourth_combo.get():
            self.error_var.set("You cannot select the same person twice")
        else:
            self.error_var.set("Saved, thank you for voting")
            with open("txt_files/Votes.txt", "a") as votefile:
                votefile.write(self.first_combo.get() + "," + self.can_position + "," + "first\n")
                votefile.write(self.second_combo.get() + "," + self.can_position + "," + "second\n")
                votefile.write(self.third_combo.get() + "," + self.can_position + "," + "third\n")
                votefile.write(self.fourth_combo.get() + "," + self.can_position + "," + "fourth\n")
            self.save_btn.config(state="disabled")
        self.can_names = []


class PresWindow(NewWindow):
    """A window containing the presidential candidates"""

    def __init__(self, master):
        NewWindow.__init__(self, master)

        self.title("Vote for your next GSU President")

        for person in self.can_list:
            if person.position == "President":
                self.can_names.append(person.name)

        self.first_combo['values'] = self.can_names
        self.second_combo['values'] = self.can_names
        self.third_combo['values'] = self.can_names
        self.fourth_combo['values'] = self.can_names

        self.can_position = "President"


class OffWindow(NewWindow):
    """A window containing the GSU Officer candidates"""

    def __init__(self, master):
        NewWindow.__init__(self, master)
        self.title("Vote for a GSU Officer")

        for person in self.can_list:
            if person.position == "GSU Officer":
                self.can_names.append(person.name)

        self.first_combo['values'] = self.can_names
        self.second_combo['values'] = self.can_names
        self.third_combo['values'] = self.can_names
        self.fourth_combo['values'] = self.can_names

        self.can_position = "GSU Officer"


class FLASWindow(NewWindow):
    """A window containing the FLAS candidates"""

    def __init__(self, master):
        NewWindow.__init__(self, master)
        self.title("Vote for Faculty Officer for Arts and Sciences (FLAS)")

        for person in self.can_list:
            if "Faculty Officer" == person.position and person.faculty == "FLAS":
                self.can_names.append(person.name)

        self.first_combo['values'] = self.can_names
        self.second_combo['values'] = self.can_names
        self.third_combo['values'] = self.can_names
        self.fourth_combo['values'] = self.can_names

        self.can_position = "Faculty Officer FLAS"

#Code by Maksim Petrov
class BUSWindow(NewWindow):
    """A window containing the BUS candidates"""

    def __init__(self, master):
        NewWindow.__init__(self, master)
        self.title("Vote for Faculty Officers for Business (BUS)")

        for person in self.can_list:
            if "Faculty Officer" == person.position and person.faculty == "BUS":
                self.can_names.append(person.name)

        self.first_combo['values'] = self.can_names
        self.second_combo['values'] = self.can_names
        self.third_combo['values'] = self.can_names
        self.fourth_combo['values'] = self.can_names

        self.can_position = "Faculty Officer BUS"

# Code by Benjamin Hawkins
class FEHWindow(NewWindow):
    """A window containing the FEH candidates"""

    def __init__(self, master):
        NewWindow.__init__(self, master)
        self.title("Vote for Faculty Officers for Education and Health (FEH)")

        for person in self.can_list:
            if "Faculty Officer" == person.position and person.faculty == "FEH":
                self.can_names.append(person.name)

        self.first_combo['values'] = self.can_names
        self.second_combo['values'] = self.can_names
        self.third_combo['values'] = self.can_names
        self.fourth_combo['values'] = self.can_names

        self.can_position = "Faculty Officer FEH"


class FESWindow(NewWindow):
    """A window containing the FES candidates"""

    def __init__(self, master):
        NewWindow.__init__(self, master)
        self.title("Vote for Faculty Officers for Engineering and Science (FES)")

        for person in self.can_list:
            if "Faculty Officer" == person.position and person.faculty == "FES":
                self.can_names.append(person.name)

        self.first_combo['values'] = self.can_names
        self.second_combo['values'] = self.can_names
        self.third_combo['values'] = self.can_names
        self.fourth_combo['values'] = self.can_names

        self.can_position = "Faculty Officer FES"

# Code by Ben Cottrell
class Visualize(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.title("Voting Results")
        self.geometry("700x300")
        self.position = ""
        self.department = ""

        self.button_frame = tk.Frame(self, bg="green")
        self.button_frame.grid(row=2, column=0, padx=10, pady=10)
        self.results_info_label = tk.Label(self,text="Below are the current results for the student union elections.\nPlease select what position you would like to see the results for:",pady=10)
        self.results_info_label.grid(row=0, column=0)

        self.president_btn = ttk.Button(self.button_frame, text="President", state='normal',command=self.btn_president)
        self.president_btn.grid(row=1, column=0)
        self.gsuOFC_btn = ttk.Button(self.button_frame, text="GSU Officer", state='normal',command=self.btn_gsuOFC)
        self.gsuOFC_btn.grid(row=1, column=1)
        self.facFLAS_btn = ttk.Button(self.button_frame, text="Faculty Officer for FLAS", state='normal',command=self.btn_facFLAS)
        self.facFLAS_btn.grid(row=1, column=2)
        self.facBUS_btn = ttk.Button(self.button_frame, text="Faculty Officer for BUS", state='normal',command=self.btn_facBUS)
        self.facBUS_btn.grid(row=1, column=3)
        self.facFEH_btn = ttk.Button(self.button_frame, text="Faculty Officer for FEH", state='normal',command=self.btn_facFEH)
        self.facFEH_btn.grid(row=1, column=4)
        self.facFES_btn = ttk.Button(self.button_frame, text="Faculty Officer for FES", state='normal',command=self.btn_facFES)
        self.facFES_btn.grid(row=1, column=5)

        self.position_info_label = tk.Label(self,text="",pady=10) #Labels that change depending on what button you press
        self.position_info_label.grid(row=3, column=0)
        self.result_label = tk.Label(self,text="",pady=10)
        self.result_label.grid(row=4, column=0)

        # Prevent multiple Toplevel windows from being created
        self.focus_set()
        self.grab_set()

    def btn_president(self):  #Functions to change what results are calculated
        self.position = "President"
        self.department = ""
        self.departmentFull = ""
        self.updateResults()
    def btn_gsuOFC(self):
        self.position = "GSU Officer"
        self.department = ""
        self.departmentFull = ""
        self.updateResults()
    def btn_facFLAS(self):
        self.position = "Faculty Officer"
        self.department = "FLAS"
        self.departmentFull = "Arts and Sciences"
        self.updateResults()
    def btn_facBUS(self):
        self.position = "Faculty Officer"
        self.department = "BUS"
        self.departmentFull = "Business"
        self.updateResults()
    def btn_facFEH(self):
        self.position = "Faculty Officer"
        self.department = "FEH"
        self.departmentFull = "Education and Health"
        self.updateResults()
    def btn_facFES(self):
        self.position = "Faculty Officer"
        self.department = "FES"
        self.departmentFull = "Engineering and Science"
        self.updateResults()

    def updateResults(self): #Updates the labels so they display the result
        if self.department == "":
            self.position_info_label["text"] = "The winner of the election for " + self.position + " is: "
            self.result_label["text"] = win_count(self.position)
        else:
            self.position_info_label["text"] = "The winner of the election for " + self.position + " of " + self.departmentFull + " is: "
            self.result_label["text"] = win_count(self.position, self.department)




