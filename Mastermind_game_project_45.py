from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
import random
from itertools import product
import numpy as np


##b = 'Blue'
##y = 'Yellow'
##o = 'Orange'
##g = 'Green'
##v = 'Violet'
##l = 'Lime'


    # Class of settings window
class FirstsSettingsWindow(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        
            # Creation of window
        self.geometry("390x380")
        self.title("Mastermind Settings")


            # Creation of start button and label
        self.start_button = ttk.Button(self, text = "Start the game", command = self.opengamewindow)
        self.start_button.place(x = 30, y = 335)
        self.good_luck_label = ttk.Label(self, text = "and Good Luck !!!")
        self.good_luck_label.place(x = 118, y = 338)

        
            # Call of menubar in settings window
        self.settingsWindowMenuBarCreation()


            # Windows settings header
        self.general_header = ttk.Label(self, text = "Settings of the game.")
        self.general_header.place(x = 10, y = 10)
        self.general_header.config(font = ("Calibri", 15))


            # User's role in the game
        self.role_header = ttk.Label(self, text = '''1. Choose your role in the game, write in the box
    'cb' for Codebreaker or 'cm' for Codemaker.''')
        self.role_header.place(x = 10, y = 50)
        self.role_textbox = ttk.Entry(self, width = 10)
        self.role_textbox.place(x = 330, y = 57)
        self.role_textbox.config(width = 5, font = ("Calibri", 12))


            # Total number of colors settings
        self.num_of_colors_header = ttk.Label(self, text = "2. Choose the number of colors in game, '5' or '6'.")
        self.num_of_colors_header.place(x = 10, y = 107)
        self.num_of_colors_textbox = ttk.Entry(self, width = 10)
        self.num_of_colors_textbox.place(x = 330, y = 105)
        self.num_of_colors_textbox.config(width = 5, font = ("Calibri", 12))


            # Code length settings
        self.code_length_header = ttk.Label(self, text = "3. Choose the code length, '3' or '4'.")
        self.code_length_header.place(x = 10, y = 157)
        self.code_length_textbox = ttk.Entry(self, width = 10)
        self.code_length_textbox.place(x = 330, y = 155)
        self.code_length_textbox.config(width = 5, font = ("Calibri", 12))


            # Duplicate colors in codemaker's code
        self.duplicate_colors_in_code_header = ttk.Label(self, text = "4. Choose duplicate colors in Codemaker's code, 'y' or 'n'.")
        self.duplicate_colors_in_code_header.place(x = 10, y = 207)
        self.duplicate_colors_in_code_textbox = ttk.Entry(self, width = 10)
        self.duplicate_colors_in_code_textbox.place(x = 330, y = 205)
        self.duplicate_colors_in_code_textbox.config(width = 5, font = ("Calibri", 12))


            # Name of user - player
        self.users_name_header = ttk.Label(self, text = "5. Insert your name.")
        self.users_name_header.place(x = 10, y = 257)
        self.users_name_textbox = ttk.Entry(self, width = 10)
        self.users_name_textbox.place(x = 290, y = 255)
        self.users_name_textbox.config(width = 10, font = ("Calibri", 12))    

        
        # Method to pass settings and open main game window 
    def opengamewindow(self):
        
        helpaboutwarnings = HelpAboutWarnings()
            # Necessary lists
        self.selected_settings = [0, 0, 0, 0, 0]
        self.selected_number_of_colors = 0
        self.selected_code_length = 0
        self.selected_duplicate_colors = 0


            # User's role in the game text box
        if self.role_textbox.get() in ["cm"]:
            self.selected_role = "cm"
            self.selected_settings[0] = self.selected_role
        elif self.role_textbox.get() in ["cb"]:
            self.selected_role = "cb"
            self.selected_settings[0] = self.selected_role


            # Total number of colors settings text box
        if self.num_of_colors_textbox.get() in ["5"]:
            self.selected_number_of_colors = 5
            self.selected_settings[1] = self.selected_number_of_colors
        elif self.num_of_colors_textbox.get() in ["6"]:
            self.selected_number_of_colors = 6
            self.selected_settings[1] = self.selected_number_of_colors

            # Code length settings text box
        if self.code_length_textbox.get() in ["3"]:
            self.selected_code_length = 3
            self.selected_settings[2] = self.selected_code_length

            # Duplicate colors in codemaker's code text box
        elif self.code_length_textbox.get() in ["4"]:
            self.selected_code_length = 4
            self.selected_settings[2] = self.selected_code_length

            # Name of user - player text box 
        if self.duplicate_colors_in_code_textbox.get() in ["y"]:
            self.selected_duplicate_colors = "True" 
            self.selected_settings[3] = self.selected_duplicate_colors
        elif self.duplicate_colors_in_code_textbox.get() in ["n"]:
            self.selected_duplicate_colors = "False" 
            self.selected_settings[3] = self.selected_duplicate_colors

            # Defensive block to avoid empty user name
        if len(self.users_name_textbox.get()) > 0:
            self.inserted_users_name = self.users_name_textbox.get()
            self.selected_settings[4] = self.inserted_users_name
            
        elif not self.users_name_textbox.get():
            self.selected_settings[4] = 0
            
            # Defensive block to avoid wrond settings input and pass settings to main game window
        if 0 not in self.selected_settings:
            mastermind = Mastermind(users_role_in_game = self.selected_settings[0], number_of_colors = self.selected_settings[1],
                           code_length = self.selected_settings[2],
                        duplicate_colors_in_code = self.selected_settings[3], username = self.selected_settings[4])
            mastermind.grab_set()
        else:
            helpaboutwarnings.errorInputWarning()


        # Method to create settings window menu bar
    def settingsWindowMenuBarCreation(self):
        helpaboutwarnings = HelpAboutWarnings()

        menubar = Menu(self)
        self.config(menu = menubar)
        file_menu = Menu(menubar, tearoff = 0)

            # Creation of file menu
        menubar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "Exit", command = self.destroy)

            # Creation of help menu
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "Help Index", command = lambda:helpaboutwarnings.helpIndex())
        helpmenu.add_command(label = "About...", command = lambda:helpaboutwarnings.about())
        menubar.add_cascade(label = "Help", menu = helpmenu)
        

    # Class about help, about and warnings in program       
class HelpAboutWarnings():
    def __init__(self):
        pass

    # About showinfo
    def about(self):
        messagebox.showinfo(title = "About", message = '''Mastermind game.

A creation of Mavrogiannis Michail
and Panourgias Panagiotis
for PLHPRO, a lesson
of Hellenic Open Univercity.
Academic Year 2021 - 2022.''')

    # helpIndex showinfo
    def helpIndex(self):
        messagebox.showinfo(title = "Rules of the game.", message = '''On first window choose the general settings of the
game. As you choose to play as 'Codemaker' pc plays
as 'Codebraker'. Create the code and let pc try to
guess it. Once you choose the role of 'Codebraker'
pc plays as 'Codemaker' respectively. Now is your turn
try guessing the code. Codebreaker has 10 tries to break
the code. Fill the empty text boxes and press the button.

Good Luck and enjoy...''')

    # Error input warning
    def errorInputWarning(self):
        messagebox.showinfo(title = "Warning", message = "Wrong input...")


    # Out of tries show info
    def endOfTheGameOutOfTries(self):
        messagebox.showinfo(title = "Out of tries!", message = f'''You lost try again...

The code was:

{' '.join(Mastermind.color)}''')


    # Winner show info 
    def endOfGameWinner(self):
        messagebox.showinfo(title = "Winner!", message = '''You won Mastermind!''')


    # Pc codebreaker winner show info
    def endOfGamePcWinner(self):
        messagebox.showinfo(title = "You lost!", message = "Pc is Mastermind!")


    # User codemaker winer show info
    def endOfGameUserWinner(self):
        messagebox.showinfo(title = "Winner", message = "You are the Codemaker and you won the pc!")


    # Duplicate color warning
    def duplicateColorsWarning(self):
        messagebox.showwarning(title = "Warning", message = "Duplicate colors are not allowed!")


    # Class with algorithm when pc is codebreaker
class Breaker():

    def __init__(self, maker_code=None, size_maker_passcode=5,
                 initial_colors=None):

        self.maker_code = maker_code
        self.size_maker_passcode = size_maker_passcode
        self.initial_colors = initial_colors
        self.colors_map = dict(zip(range(1, len(self.initial_colors) + 1), self.initial_colors))

    # 
    def initialize_move(self):
        combinations_of_breaker_code = list(product(range(1, self.size_maker_passcode + 1),
                                                    repeat=self.size_maker_passcode))
        self.move = random.sample(combinations_of_breaker_code, 1)
        self.move = [list(x) for x in self.move][0]
        return [self.colors_map[x] for x in self.move]

    # 
    def next_move(self, move):
        breaker_pass = [0] * self.size_maker_passcode
        for num in range(len(move)):
            if move[num] == self.maker_code[num]:
                breaker_pass[num] = self.maker_code[num]
            else:
                breaker_pass[num] = self.colors_map[random.randint(1, len(self.initial_colors))]

        return breaker_pass
    

        
    # Class about main Mastermind game window 
class Mastermind(tk.Toplevel):
    
    
    def __init__(self, users_role_in_game, number_of_colors, code_length, duplicate_colors_in_code, username):


            # Main counter
        self.counter = 0
        
        self.users_role_in_game = users_role_in_game
        self.number_of_colors = number_of_colors
        self.code_length = code_length
        self.duplicate_colors_in_code = duplicate_colors_in_code
        self.username = username


            # Available colors list, shorted colors list and list with adresses about labels possitions
        self.available_colors = ['Blue', 'Yellow', 'Orange', 'Green', 'Violet', 'Lime'][:self.number_of_colors]
        self.shorted_colors = ['b', 'y', 'o', 'g', 'v', 'l'][:self.number_of_colors]
        self.creationOfCbanswer_list = [410, 370, 330, 290, 250, 210, 170, 130, 90, 50]


            # Necessary lists
        Mastermind.color = []

        self.guesses_list = []
        self.feedback_list = []
        self.label_answer_cb_list = []
        self.label_feedback_list = []
        self.user_codemaker_list = []
        self.user_cm_feedback_list = []

        super().__init__()

           
            # Call of menubar
        self.topWindowCreationMenuBar()

        
            # Call of answer and feedback number of labels
        self.creationOfAnswerAndFeedbackNumAndLabels()


            # When User is Codebreaker
        if self.users_role_in_game == "cb":

            
                # Creation of main window
            self.geometry("550x620")
            self.title('Mastermind game')
            self.configure(background = "PeachPuff3")


                # Creation of User - Codebrekaer's Guess button
            self.guess_button = ttk.Button(self, text = "Guess", command = lambda:self.commandOfGuessButton(creationofcode = self.creationOfCode))


                # Creation of PC - Codemaker's code.
            self.creationOfCode = self.creationOfCode(colors = self.available_colors, duplicate_colors_in_code
                                             = self.duplicate_colors_in_code)
            self.config(width = 8, height = 2)
            self.guess_button.place(x = 300, y = 480)


                # Color table information
            self.label_info_head_upper = Label(self, text = "Color table info.", font = ("Calibri", 12),
                                         background = "PeachPuff3")
            self.label_info_head_upper.place(x = 8, y = 518)
            self.label_info_head_down = Label(self, text = "The available colors to choose are bellow:",
                                              font = ("Calibri", 12),
                                         background = "PeachPuff3")
            self.label_info_head_down.place(x = 8, y = 538)

            if self.number_of_colors == 5:
                self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet",
                                    font = ("Calibri", 12), background = "PeachPuff3")
                self.label_info.place(x = 8, y = 558)
            else:
                self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet, l = Lime",
                                    font = ("Calibri", 12), background = "PeachPuff3")
                self.label_info.place(x = 8, y = 558)


            self.role_in_game_info = Label(self, text = "**** {} is the 'Codebreaker' and pc is the 'Codemaker'. ****". format(self.username),
                                           font = ("Calibri", 12), background = "PeachPuff3", foreground='green')
            self.role_in_game_info.place(x = 8, y = 590)

            
                # Creation of user - Codebreaker's textboxes
            if self.code_length == 3:
                self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
                self.label_cb_ins_box_head.place(x = 30, y = 455)
                self.textbox_cb_1 = ttk.Entry(self)
                self.textbox_cb_1.place(x = 30, y = 480)
                self.textbox_cb_1.config(width = 5, font = ("Calibri", 12))

                self.textbox_cb_2 = ttk.Entry(self)
                self.textbox_cb_2.place(x = 80, y = 480)
                self.textbox_cb_2.config(width = 5, font = ("Calibri", 12))
            
                self.textbox_cb_3 = ttk.Entry(self)
                self.textbox_cb_3.place(x = 130, y = 480)
                self.textbox_cb_3.config(width = 5, font = ("Calibri", 12))


            else:
                self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
                self.label_cb_ins_box_head.place(x = 30, y = 455)
                self.textbox_cb_1 = ttk.Entry(self)
                self.textbox_cb_1.place(x = 30, y = 480)
                self.textbox_cb_1.config(width = 5, font = ("Calibri", 12))

                self.textbox_cb_2 = ttk.Entry(self)
                self.textbox_cb_2.place(x = 80, y = 480)
                self.textbox_cb_2.config(width = 5, font = ("Calibri", 12))
            
                self.textbox_cb_3 = ttk.Entry(self)
                self.textbox_cb_3.place(x = 130, y = 480)
                self.textbox_cb_3.config(width = 5, font = ("Calibri", 12))
                self.textbox_cb_4 = ttk.Entry(self)
                self.textbox_cb_4.place(x = 180, y = 480)
                self.textbox_cb_4.config(width = 5, background = "SkyBlue3", font = ("Calibri", 12))


            # When User is Codemaker.
        elif self.users_role_in_game == "cm":


                # Creation of main window
            self.geometry("550x730")
            self.title('Mastermind game')
            self.configure(background = "PeachPuff3")


                # Creation of User - Codebreaker's Guess button
            self.creation_code_button = ttk.Button(self, text = "Create the code",
                                                   command = lambda:self.creationUsersCmCodeButtonCommand())
            self.config(width = 8, height = 2)
            self.creation_code_button.place(x = 300, y = 480)


                # color table information
            self.label_info_head_upper = Label(self, text = "Color table info.", font = ("Calibri", 12),
                                         background = "PeachPuff3")
            self.label_info_head_upper.place(x = 8, y = 618)
            self.label_info_head_down = Label(self, text = "The available colors to choose are bellow:",
                                              font = ("Calibri", 12),
                                         background = "PeachPuff3")
            self.label_info_head_down.place(x = 8, y = 638)
            
            
            if self.number_of_colors == 5:
                self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet",
                                    font = ("Calibri", 12), background = "PeachPuff3")
                self.label_info.place(x = 8, y = 658)
            else:
                self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet, l = Lime",
                                    font = ("Calibri", 12), background = "PeachPuff3")
                self.label_info.place(x = 8, y = 658)
                

            self.label_feedback_info_header = Label(self, text = "The available feedback colors are: r = Red, w = White and empty textbox.",
                                                    font = ("Calibri", 12), background = "PeachPuff3")
            self.label_feedback_info_header.place(x = 8, y = 590)

            self.role_in_game_info = Label(self, text = "**** {} is the 'Codemaker' and pc is the 'Codebreaker'. ****". format(self.username),
                                           font = ("Calibri", 12), background = "PeachPuff3", foreground='green')
            self.role_in_game_info.place(x = 8, y = 690)
            

            if self.code_length == 3:
                self.label_cm_ins_box_head = Label(self, text = "Codemaker's code.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
                self.label_cm_ins_box_head.place(x = 30, y = 455)
                self.textbox_cm_1 = ttk.Entry(self)
                self.textbox_cm_1.place(x = 30, y = 480)
                self.textbox_cm_1.config(width = 5, font = ("Calibri", 12))

                self.textbox_cm_2 = ttk.Entry(self)
                self.textbox_cm_2.place(x = 80, y = 480)
                self.textbox_cm_2.config(width = 5, font = ("Calibri", 12))
            
                self.textbox_cm_3 = ttk.Entry(self)
                self.textbox_cm_3.place(x = 130, y = 480)
                self.textbox_cm_3.config(width = 5, font = ("Calibri", 12))


                # Creation of user's feedback entry boxes
                self.textbox_cm_feedback_1 = ttk.Entry(self)
                self.textbox_cm_feedback_1.place(x = 30, y = 550)
                self.textbox_cm_feedback_1.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_2 = ttk.Entry(self)
                self.textbox_cm_feedback_2.place(x = 80, y = 550)
                self.textbox_cm_feedback_2.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_3 = ttk.Entry(self)
                self.textbox_cm_feedback_3.place(x = 130, y = 550)
                self.textbox_cm_feedback_3.config(width = 5, font = ("Calibri", 12), state= "disabled")

                

            else:
                self.label_cm_ins_box_head = Label(self, text = "Codemaker's code.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
                self.label_cm_ins_box_head.place(x = 30, y = 455)
                self.textbox_cm_1 = ttk.Entry(self)
                self.textbox_cm_1.place(x = 30, y = 480)
                self.textbox_cm_1.config(width = 5, font = ("Calibri", 12))

                self.textbox_cm_2 = ttk.Entry(self)
                self.textbox_cm_2.place(x = 80, y = 480)
                self.textbox_cm_2.config(width = 5, font = ("Calibri", 12))
            
                self.textbox_cm_3 = ttk.Entry(self)
                self.textbox_cm_3.place(x = 130, y = 480)
                self.textbox_cm_3.config(width = 5, font = ("Calibri", 12))
                self.textbox_cm_4 = ttk.Entry(self)
                self.textbox_cm_4.place(x = 180, y = 480)
                self.textbox_cm_4.config(width = 5, background = "SkyBlue3", font = ("Calibri", 12))


                # Creation of user's feedback entry boxes
                self.textbox_cm_feedback_1 = ttk.Entry(self)
                self.textbox_cm_feedback_1.place(x = 30, y = 550)
                self.textbox_cm_feedback_1.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_2 = ttk.Entry(self)
                self.textbox_cm_feedback_2.place(x = 80, y = 550)
                self.textbox_cm_feedback_2.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_3 = ttk.Entry(self)
                self.textbox_cm_feedback_3.place(x = 130, y = 550)
                self.textbox_cm_feedback_3.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_4 = ttk.Entry(self)
                self.textbox_cm_feedback_4.place(x = 180, y = 550)
                self.textbox_cm_feedback_4.config(width = 5, font = ("Calibri", 12), state= "disabled")

                

            self.label_cm_ins_box_header = Label(self, text = "Codemaker's feedback input boxes.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
            self.label_cm_ins_box_header.place(x = 30, y = 525)

            self.next_move_button = Button(self, text = "Give feedback", command = lambda:self.commandOfGiveFeedbackButton())
            self.next_move_button.place(x = 300, y = 550)
            self.next_move_button.config(width = 14, height = 1)
            self.next_move_button['state'] = DISABLED

        # Method of Give feedback button
    def commandOfGiveFeedbackButton(self):
        helpaboutwarnings = HelpAboutWarnings()
        
        usercodemakerfeedback = self.userCodemakerFeedback()
        
        if self.validationOfInput(returnablevalue = usercodemakerfeedback) == 1:
            self.answerAndFeedbackLabels(feedback = usercodemakerfeedback, answer = self.ai_solver_run())
        else:
            helpaboutwarnings.errorInputWarning()

        
        # Method for create the code button of user - Codemaker
    def creationUsersCmCodeButtonCommand(self):

        helpaboutwarnings = HelpAboutWarnings()

        self.user_codemaker_list.clear()
        if self.code_length == 3:
            
                # textbox_cm_1 check
            users_cm_input_1 = self.textbox_cm_1.get()
            if users_cm_input_1 in self.shorted_colors:
                if users_cm_input_1 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_1 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_1 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_1 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_1 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_1 == "l": self.user_codemaker_list.append("Lime")
    
                # textbox_cm_2 check
            users_cm_input_2 = self.textbox_cm_2.get()
            if users_cm_input_2 in self.shorted_colors:
                if users_cm_input_2 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_2 == "y": self.user_codemaker_list.append("Yellow")
                elif users_cm_input_2 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_2 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_2 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_2 == "l": self.user_codemaker_list.append("Lime")

                # textbox_cm_3 check
            users_cm_input_3 = self.textbox_cm_3.get()
            if users_cm_input_3 in self.shorted_colors:
                if users_cm_input_3 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_3 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_3 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_3 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_3 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_3 == "l": self.user_codemaker_list.append("Lime")

                # Defensive block about validation of input of user - Codemaker code
            if self.validationOfInput(returnablevalue = self.user_codemaker_list) == 1:
                self.user_codemaker_set = set(self.user_codemaker_list)

                # Defensive block about validation of duplicate colors in input of user - Codemaker code
                if self.duplicate_colors_in_code == "False" and len(self.user_codemaker_list) != len(self.user_codemaker_set):
                    helpaboutwarnings.duplicateColorsWarning()
                else:
                    self.creation_code_button.destroy()
                    self.textbox_cm_1.destroy()
                    self.textbox_cm_2.destroy()
                    self.textbox_cm_3.destroy()
                    self.users_cm_code_label = ttk.Label(self, text = self.user_codemaker_list, font = ("Calibri", 13), width = 22,
                                                         relief = SUNKEN, background = "cyan")
                    self.users_cm_code_label.place(x = 30, y = 480)
                    self.textbox_cm_feedback_1.config(state = "enabled")
                    self.textbox_cm_feedback_2.config(state = "enabled")
                    self.textbox_cm_feedback_3.config(state = "enabled")
                    self.next_move_button['state'] = NORMAL
                    
                    self.answerAndFeedbackLabels(feedback = "", answer = self.ai_solver_run())

                    return self.user_codemaker_list                    

            else:
                helpaboutwarnings.errorInputWarning()
                


        else:
                # textbox_cm_1 check 
            users_cm_input_1 = self.textbox_cm_1.get()
            if users_cm_input_1 in self.shorted_colors:
                if users_cm_input_1 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_1 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_1 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_1 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_1 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_1 == "l": self.user_codemaker_list.append("Lime")
    
                # textbox_cm_2 check
            users_cm_input_2 = self.textbox_cm_2.get()
            if users_cm_input_2 in self.shorted_colors:
                if users_cm_input_2 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_2 == "y": self.user_codemaker_list.append("Yellow")
                elif users_cm_input_2 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_2 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_2 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_2 == "l": self.user_codemaker_list.append("Lime")

                # textbox_cm_3 check 
            users_cm_input_3 = self.textbox_cm_3.get()
            if users_cm_input_3 in self.shorted_colors:
                if users_cm_input_3 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_3 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_3 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_3 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_3 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_3 == "l": self.user_codemaker_list.append("Lime")

                # textbox_cm_4 check
            users_cm_input_4 = self.textbox_cm_4.get()
            if users_cm_input_4 in self.shorted_colors:
                if users_cm_input_4 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_4 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_4 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_4 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_4 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_4 == "l": self.user_codemaker_list.append("Lime")


                # Defensive block about validation of input of user - Codemaker code
            if self.validationOfInput(returnablevalue = self.user_codemaker_list) == 1:
                self.user_codemaker_set = set(self.user_codemaker_list)

                # Defensive block about validation of duplicate colors in input of user - Codemaker code
                if self.duplicate_colors_in_code == "False" and len(self.user_codemaker_list) != len(self.user_codemaker_set):
                    helpaboutwarnings.duplicateColorsWarning()
                else:
                    self.creation_code_button.destroy()
                    self.textbox_cm_1.destroy()
                    self.textbox_cm_2.destroy()
                    self.textbox_cm_3.destroy()
                    self.textbox_cm_4.destroy()
                    self.users_cm_code_label = ttk.Label(self, text = self.user_codemaker_list, font = ("Calibri", 13), width = 22,
                                                             relief = SUNKEN, background = "cyan")
                    self.users_cm_code_label.place(x = 30, y = 480)
                    self.textbox_cm_feedback_1.config(state = "enabled")
                    self.textbox_cm_feedback_2.config(state = "enabled")
                    self.textbox_cm_feedback_3.config(state = "enabled")
                    self.textbox_cm_feedback_4.config(state = "enabled")
                    self.next_move_button['state'] = NORMAL

                    self.answerAndFeedbackLabels(feedback = "", answer = self.ai_solver_run())

                    return self.user_codemaker_list

            else:
                helpaboutwarnings.errorInputWarning()
                

        # Method about feedback of user - Codemaker 
    def userCodemakerFeedback(self):
        self.user_cm_feedback_list.clear()
        
        if self.code_length == 3:
            
                # textbox_1 check
            users_cm_feed_input_1 = self.textbox_cm_feedback_1.get()
            if users_cm_feed_input_1 in ["r", "w", ""]:
                if users_cm_feed_input_1 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_1 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_1 == "": self.user_cm_feedback_list.append("")
    
                # textbox_2 check
            users_cm_feed_input_2 = self.textbox_cm_feedback_2.get()
            if users_cm_feed_input_2 in ["r", "w", ""]:
                if users_cm_feed_input_2 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_2 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_2 == "": self.user_cm_feedback_list.append("")

                # textbox_3 check
            users_cm_feed_input_3 = self.textbox_cm_feedback_3.get()
            if users_cm_feed_input_3 in ["r", "w", ""]:
                if users_cm_feed_input_3 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_3 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_3 == "": self.user_cm_feedback_list.append("")

            return self.user_cm_feedback_list


        else:
                # textbox_1 check
            users_cm_feed_input_1 = self.textbox_cm_feedback_1.get()
            if users_cm_feed_input_1 in ["r", "w", ""]:
                if users_cm_feed_input_1 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_1 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_1 == "": self.user_cm_feedback_list.append("")
    
                # textbox_2 check
            users_cm_feed_input_2 = self.textbox_cm_feedback_2.get()
            if users_cm_feed_input_2 in ["r", "w", ""]:
                if users_cm_feed_input_2 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_2 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_2 == "": self.user_cm_feedback_list.append("")

                # textbox_3 check
            users_cm_feed_input_3 = self.textbox_cm_feedback_3.get()
            if users_cm_feed_input_3 in ["r", "w", ""]:
                if users_cm_feed_input_3 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_3 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_3 == "": self.user_cm_feedback_list.append("")

                # textbox_4 check
            users_cm_feed_input_4 = self.textbox_cm_feedback_4.get()
            if users_cm_feed_input_4 in ["r", "w", ""]:
                if users_cm_feed_input_4 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_4 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_4 == "": self.user_cm_feedback_list.append("")

            return self.user_cm_feedback_list

        # Method which creates breaker's object and generates color combinations.
    def ai_solver_run(self):
        breaker = Breaker(maker_code = self.user_codemaker_list, size_maker_passcode = self.code_length,
                                                                              initial_colors = self.available_colors)

        if self.counter == 0:
            self.guesses_list = breaker.initialize_move()
        else:
            self.guesses_list = breaker.next_move(self.guesses_list)

        return self.guesses_list


        # Method of new game menu bar button
    def newGameMenuButton(self):
        self.destroy()
        Mastermind(self.users_role_in_game, self.number_of_colors, self.code_length, self.duplicate_colors_in_code, self.username)

        
        # Method of Guess button
    def commandOfGuessButton(self, creationofcode):
        helpaboutwarnings = HelpAboutWarnings()
        
        codebreaker = self.codeBreaker()
            
        if self.validationOfInput(returnablevalue = codebreaker) == 1:
            printingcode = self.printingcode(copiedguess = codebreaker, copiedcode = creationofcode)
            answerandfeedbacklabels = self.answerAndFeedbackLabels(feedback = printingcode,
                                                                           answer = codebreaker)
        else:
            helpaboutwarnings.errorInputWarning()


        # Method of validation input   
    def validationOfInput(self, returnablevalue):        
        returnablevalue = list(returnablevalue)
        if len(returnablevalue) != self.code_length:
            return 2 # It means False
        elif len(returnablevalue) == self.code_length:
            return 1 # It means True



        # Method of creation code of pc - Codemaker, with duplicate or not colors
    def creationOfCode(self, colors, duplicate_colors_in_code):
        available_colors_list = list(colors)
        

        if len(Mastermind.color) == self.code_length:
            return Mastermind.color

        if duplicate_colors_in_code == "False":
            Mastermind.color = random.sample(available_colors_list, k = self.code_length)
            return Mastermind.color
        
        elif duplicate_colors_in_code == "True":
            Mastermind.color = random.choices(available_colors_list, k = self.code_length)
            return Mastermind.color


        # Method about creation of answer and feedback labels in game
    def creationOfAnswerAndFeedbackNumAndLabels(self):
        self.label_head_cb = Label(self, text = "Codebreaker's answers.", font = ("Calibri", 13),
                                   background = "PeachPuff3")
        self.label_head_cb.place(x = 8, y = 10)

        self.label_feedback_head = Label(self, text = "Codemaker's feedback.", font = ("Calibri", 13),
                                         background = "PeachPuff3")
        self.label_feedback_head.place(x = 300, y = 10)
        
        for _ in range(10):
            self.label_cb = Label(self, text = str(_ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_cb.place(x = 8, y = self.creationOfCbanswer_list[_])

            self.label_feedback = Label(self, text = str(_ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_feedback.place(x = 300, y = self.creationOfCbanswer_list[_])
            
            self.label_feedback_list.append(Label(self, background = "NavajoWhite2",
                                                        font = ("Calibri", 12), width = 24))
            self.label_feedback_list[_].place(x = 320, y = self.creationOfCbanswer_list[_])

            self.label_answer_cb_list.append(Label(self, background = "light grey",
                                                         font = ("Calibri", 12), width = 24))
            self.label_answer_cb_list[_].place(x = 30, y = self.creationOfCbanswer_list[_])


        # Answer and feedback printing in labels
    def answerAndFeedbackLabels(self, feedback, answer):
        helpaboutwarnings = HelpAboutWarnings()
        
        feedback = list(feedback)   
        answer = list(answer)

        if self.users_role_in_game == "cm":
            if self.counter < 10 and self.user_cm_feedback_list.count("Red") != self.code_length:
                self.label_answer_cb_list[self.counter].config(text = " ".join(answer), background = "LightSteelBlue3", relief = SUNKEN)
                self.label_answer_cb_list[self.counter].place(x = 30, y = self.creationOfCbanswer_list[self.counter])

            if self.counter >= 1:
                if self.counter <= 10:
                    self.label_feedback_list[self.counter - 1].config(text = " ".join(feedback), relief = SUNKEN)
                    self.label_feedback_list[self.counter - 1].place(x = 320, y = self.creationOfCbanswer_list[self.counter - 1])
                    #self.label_feedback_list[Mastermind.counter - 1].config(relief = SUNKEN)

                    if self.user_cm_feedback_list.count("Red") == self.code_length:
                        self.next_move_button['state'] = DISABLED
                        helpaboutwarnings.endOfGamePcWinner()

                    elif self.counter == 10:
                        self.next_move_button['state'] = DISABLED
                        helpaboutwarnings.endOfGameUserWinner()

            self.counter += 1


        elif self.users_role_in_game == "cb":
            if self.counter <= 9:
                self.label_answer_cb_list[self.counter].config(text = " ".join(answer), background = "LightSteelBlue3", relief = SUNKEN)
                self.label_answer_cb_list[self.counter].place(x = 30, y = self.creationOfCbanswer_list[self.counter])

            if self.counter <= 9:
                self.label_feedback_list[self.counter].config(text = " ".join(feedback))
                self.label_feedback_list[self.counter].place(x = 320, y = self.creationOfCbanswer_list[self.counter])
                self.label_feedback_list[self.counter].config(relief = SUNKEN)

                if self.feedback_list.count("Red") == self.code_length:
                    self.guess_button['state'] = DISABLED
                    helpaboutwarnings.endOfGameWinner()

                elif self.counter == 9:
                    self.guess_button['state'] = DISABLED
                    helpaboutwarnings.endOfTheGameOutOfTries()

            self.counter += 1


        
        # Method that creates menu bar of main game window      
    def topWindowCreationMenuBar(self):
        helpaboutwarnings = HelpAboutWarnings()
        
        menubar = Menu(self)
        self.config(menu = menubar)
        file_menu = Menu(menubar, tearoff = 0)

            # Creation of file menu
        menubar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "New", command = self.newGameMenuButton)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = self.destroy)

            # Creation of help menu
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "Help Index", command = lambda:helpaboutwarnings.helpIndex())
        helpmenu.add_command(label = "About...", command = lambda:helpaboutwarnings.about())
        menubar.add_cascade(label = "Help", menu = helpmenu)

    

    def codeBreaker(self):
        self.guesses_list.clear()        
        
        if self.code_length == 3:
            
                # textbox_1 check
            users_input_1 = self.textbox_cb_1.get()
            if users_input_1 in self.shorted_colors:
                if users_input_1 == "b": self.guesses_list.append("Blue")
                elif users_input_1 == "y": self.guesses_list.append("Yellow")   
                elif users_input_1 == "o": self.guesses_list.append("Orange")
                elif users_input_1 == "v": self.guesses_list.append("Violet")
                elif users_input_1 == "g": self.guesses_list.append("Green")
                elif users_input_1 == "l": self.guesses_list.append("Lime")
    
                # textbox_2 check
            users_input_2 = self.textbox_cb_2.get()
            if users_input_2 in self.shorted_colors:
                if users_input_2 == "b": self.guesses_list.append("Blue")
                elif users_input_2 == "y": self.guesses_list.append("Yellow")
                elif users_input_2 == "o": self.guesses_list.append("Orange")
                elif users_input_2 == "v": self.guesses_list.append("Violet")
                elif users_input_2 == "g": self.guesses_list.append("Green")
                elif users_input_2 == "l": self.guesses_list.append("Lime")

                # textbox_3 check
            users_input_3 = self.textbox_cb_3.get()
            if users_input_3 in self.shorted_colors:
                if users_input_3 == "b": self.guesses_list.append("Blue")
                elif users_input_3 == "y": self.guesses_list.append("Yellow")   
                elif users_input_3 == "o": self.guesses_list.append("Orange")
                elif users_input_3 == "v": self.guesses_list.append("Violet")
                elif users_input_3 == "g": self.guesses_list.append("Green")
                elif users_input_3 == "l": self.guesses_list.append("Lime")
            return self.guesses_list



        else:
                # textbox_1 check
            users_input_1 = self.textbox_cb_1.get()
            if users_input_1 in self.shorted_colors:
                if users_input_1 == "b": self.guesses_list.append("Blue")
                elif users_input_1 == "y": self.guesses_list.append("Yellow")   
                elif users_input_1 == "o": self.guesses_list.append("Orange")
                elif users_input_1 == "v": self.guesses_list.append("Violet")
                elif users_input_1 == "g": self.guesses_list.append("Green")
                elif users_input_1 == "l": self.guesses_list.append("Lime")
    
                # textbox_2 check
            users_input_2 = self.textbox_cb_2.get()
            if users_input_2 in self.shorted_colors:
                if users_input_2 == "b": self.guesses_list.append("Blue")
                elif users_input_2 == "y": self.guesses_list.append("Yellow")
                elif users_input_2 == "o": self.guesses_list.append("Orange")
                elif users_input_2 == "v": self.guesses_list.append("Violet")
                elif users_input_2 == "g": self.guesses_list.append("Green")
                elif users_input_2 == "l": self.guesses_list.append("Lime")

                # textbox_3 check
            users_input_3 = self.textbox_cb_3.get()
            if users_input_3 in self.shorted_colors:
                if users_input_3 == "b": self.guesses_list.append("Blue")
                elif users_input_3 == "y": self.guesses_list.append("Yellow")   
                elif users_input_3 == "o": self.guesses_list.append("Orange")
                elif users_input_3 == "v": self.guesses_list.append("Violet")
                elif users_input_3 == "g": self.guesses_list.append("Green")
                elif users_input_3 == "l": self.guesses_list.append("Lime")
                # textbox_4 check
            users_input_4 = self.textbox_cb_4.get()
            if users_input_4 in self.shorted_colors:
                if users_input_4 == "b": self.guesses_list.append("Blue")
                elif users_input_4 == "y": self.guesses_list.append("Yellow")   
                elif users_input_4 == "o": self.guesses_list.append("Orange")
                elif users_input_4 == "v": self.guesses_list.append("Violet")
                elif users_input_4 == "g": self.guesses_list.append("Green")
                elif users_input_4 == "l": self.guesses_list.append("Lime")  
            return self.guesses_list 

        
        # Method that checks code and guess and give feedback when User is Codebreaker
    def printingcode(self, copiedguess, copiedcode):
        
        self.feedback_list.clear()
        guess = list(copiedguess)
        code = list(copiedcode)

        for num in range(len(guess)):
            if guess[num] == code[num]:
                guess[num] = 1
                code[num] = 2
                self.feedback_list.append("Red")

        for num in range(len(guess)):
            if guess[num] in code:
                self.feedback_list.append("White")

        return self.feedback_list
        
    
        
if __name__ == "__main__":

    firstsettingswindow = FirstsSettingsWindow()
    firstsettingswindow.mainloop()


    
