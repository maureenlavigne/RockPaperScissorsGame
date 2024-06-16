# UI of game on Tkinter
from main import *

# Import the tkinter module for GUI
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Jeu : Pierre Feuille Ciseau.")

# Create an input field
#entry = tk.Entry(root, highlightcolor="black", highlightthickness=5,
#                 width=70, bg="yellow", font=("Times", 15, "bold"))
#entry.grid(row=0, column=0, columnspan=3)

# Create Label
label = tk.Label(root, text="Clique sur jouer pour commencer la partie !", highlightcolor="black", highlightthickness=5,
                 width=70, bg="yellow", font=("Times", 15, "bold"))
label.grid(row=0, column=0, columnspan=3)

# Create buttons for choices (pierre, feuille, ciseau)
buttons = [
    "pierre", "feuille", "ciseau",
]
row, col = 1, 0

for button in buttons:
    print(button)
    tk.Button(root, text=button, bg="yellow", padx=20, pady=20, font=("Times", 16, "bold"),
              command=lambda button=button: button_click(button)).grid(row=row, column=col, columnspan=1, sticky="ew")
    col += 1
    if col > 2:
        col = 0
        row += 1


# Create a Continue button
tk.Button(root, text="jouer", width=15, padx=20, pady=20, bg="yellow", font=("Times", 16, "bold"),
          command=lambda: button_click("jouer")).grid(row=4, column=0, columnspan=3, sticky="ew")

# When open window
# Joke UI(entry)
#def jokeUI():
#    label.config(text="")
#    label.after(500,label.config(text="On va jouer à pierre feuille ciseau !"))
#    label.after(500,label.config(text="Ready ?"))
#   label.after(500,label.config(text="3..."))
#    label.after(500,label.config(text="2..."))
#    label.after(500,label.config(text="1..."))
#    label.after(500,label.config(text="Clique sur ton choix :"))

def startGame():
    label.config(text="Clique sur ton choix :")

# Return -1 if draw, 0 if user wins, 1 if computer wins
def result_duel(user,computer):
    if user == computer:
        return -1
    if user == "pierre" and computer == "ciseau":
        return 0
    if user == "pierre" and computer == "feuille":
        return 1
    if user == "ciseau" and computer == "feuille":
        return 0
    if user == "ciseau" and computer == "pierre":
        return 1
    if user == "feuille" and computer == "ciseau":
        return 1
    if user == "feuille" and computer == "pierre":
        return 0
def button_click(value):
    print(value)
    match value:
        case "jouer":
            startGame()
        case "pierre":
            print(value)
            user = "pierre"
            match random.randrange(1, 3):
                case 1:
                    computer_answer = "pierre"
                case 2:
                    computer_answer = "feuille"
                case 3:
                    computer_answer = "ciseau"
                case _:
                    exit(-1)
            result = result_duel(user, computer_answer)
            match result:
                case -1:
                    label.config(text=computer_answer+" ! Egalité ! On recommence ?")
                case 0:
                    label.config(text=computer_answer+" ! Tu as gagné ! On recommence ?")
                case 1:
                    label.config(text=computer_answer+"! Tu as perdu ! On recommence ?")
#        case "feuille":
#            # if partie commencée
#                # jouer pierre
#        case "ciseau":
#            # if partie commencée
#                # jouer pierre
#        case _:


# Start the Tkinter main loop
root.mainloop()