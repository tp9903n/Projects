# Code by Benjamin Hawkins bh1625a
import tkinter as tk
import tkinter.ttk as ttk
from Submenus import CastVoteWindow
from Submenus import Visualize
from CurrentDate import TimerDate
from Task2 import Comments

class MainGUI(tk.Tk):
    """The main menu GUI for the GSU voting system
    ----------
    Methods
    ----------
    cast_votes(self)
        Opens a new window so that a voter can vote for a candidate
    """

    def __init__(self):
        super().__init__()
        self.title("GSU Voting System")
        self.geometry("700x300")
        main_menu_label = tk.Label(self,
                                   text="Welcome to the GSU Voting System.\n Please login and then cast your vote",
                                   pady=10)
        main_menu_label.grid(row=0, column=0)

        # A frame to hold the login and password fields
        self.login_frame = tk.Frame(self)
        self.login_frame.grid(row=1, column=0, pady=10, padx=10)
        self.username_label = tk.Label(self.login_frame, text="Username: ", padx=10)
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame, bg="white", fg="black")
        self.username_entry.grid(row=0, column=1)
        self.pass_label = tk.Label(self.login_frame, text="Password: ", padx=13)
        self.pass_label.grid(row=1, column=0)
        self.pass_entry = tk.Entry(self.login_frame, show="*", bg="white", fg="black")
        self.pass_entry.grid(row=1, column=1)
        self.error_label = tk.Label(self.login_frame, text="",
                                    fg='red')  # Error labels have their values changed by the login function
        self.error_label.grid(row=1, column=4)
        self.error_label2 = tk.Label(self.login_frame, text="", fg='red')
        self.error_label2.grid(row=0, column=4)
        self.login_btn = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.login_btn.grid(row=3, column=2, sticky="E")

        # A frame to hold all of the buttons
        self.button_frame = tk.Frame(self, bg="green")
        self.button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.cast_btn = ttk.Button(self.button_frame, text="Cast Votes", command=self.cast_votes, state='disabled')
        self.cast_btn.grid(row=0, column=0, sticky='W')
        self.visualise_btn = ttk.Button(self.button_frame, text="Visualise Results", state='disabled',command=self.Visualize_results)
        self.visualise_btn.grid(row=2, column=0)
        self.comments_btn = ttk.Button(self.button_frame, text="Make Comments", state='normal',command=self.Comments)
        self.comments_btn.grid(row=3, column=0)
        self.exit_btn = ttk.Button(self.button_frame, text="Exit", command=self.quit)
        self.exit_btn.grid(row=3, column=1, sticky='E')

    # Source: https://stackoverflow.com/questions/46738966/how-to-check-text-file-for-usernames-and-passwords
    # The code was incorporated then heavily edited, the part used was pretty much just checking if the username/password is in the list in the correct index
# Code by Ben Cottrell
    def login(self):
        username = self.username_entry.get()
        password = self.pass_entry.get()
        studentInfo = open("txt_files/StudentVoters.txt",
                           "r").readlines()  # reads every line of username password txt file
        for line in studentInfo:
            election = TimerDate()
            if election.within_election_period():
                info = line.split()
            #            print(studentInfo)

                if username == info[0] and password == info[1] and (info[2] == "false"):  # Checks every line in username password txt for a matching username and pass, aswell as checking they have not voted already
                #                print("Sucessful Login!")
                    self.cast_btn["state"] = "normal"
                    self.visualise_btn["state"] = "normal"
                    self.error_label["text"] = ""
                    self.error_label2["text"] = ""
                    return True
                    break
                if username == info[0] and password == info[1] and (info[2] == "true"):  # Checks every line in username password txt for a matching username and pass as well as if they have voted
                    # print("Sucessful login but you have already voted!")
                    self.cast_btn["state"] = "disabled"
                    self.visualise_btn["state"] = "normal"
                    self.error_label["text"] = ""
                    self.error_label2["text"] = "Sucessful login but you have already voted!"
                    return True
                    break
                elif username == info[0]:  # wrong pass but correct username, allows user to enter details again
                    # print("Unsucessful Login, invalid password.")
                    self.cast_btn["state"] = "disabled"
                    self.visualise_btn["state"] = "disabled"
                    self.error_label["text"] = "Unsucessful Login, invalid password"
                    self.error_label2["text"] = ""
                    break
                elif username not in info:  # Username doesn't exist
                    # print("Unsucessful Login, you are not eligble to vote.")
                    self.cast_btn["state"] = "disabled"
                    self.visualise_btn["state"] = "disabled"
                    self.error_label2["text"] = "Unsucessful Login, username invalid or you are not eligble to vote."
                    self.error_label["text"] = ""
            else:
                self.error_label["text"] = "Voting window between 09:00 and 22:00 28th January 2020"

    def cast_votes(self):
        """Opens a new toplevel window so that a voter can vote for a candidate"""
        CastVoteWindow(self)
    def Visualize_results(self):
        Visualize(self)
    def Comments(self):
        Comments(self)

# Code by Benjamin Hawkins bh1625a
# If running the file directly open the main menu GUI.
if __name__ == '__main__':
    root = MainGUI()
    root.mainloop()