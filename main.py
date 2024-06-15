
import time
import random

def slow_writing(txt, speed=0.05):
    for c in txt:
        print(c, end="")
        time.sleep(speed)
    print()

# Return -1 if draw, 0 if user wins, 1 if computer wins
def result_duel(user,computer):
    slow_writing(computer+"!")
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




slow_writing("On va jouer à pierre feuille ciseau !")
time.sleep(2)
slow_writing("Ready ?")
time.sleep(2)
slow_writing("3...")
time.sleep(1)
slow_writing("2...")
time.sleep(1)
slow_writing("1...")
time.sleep(1)
slow_writing("Tape ton choix au clavier, sans majuscule :")

answer1 = input()

if answer1 == "pierre":
    slow_writing("feuille ! J'ai gagné.")

if answer1 == "feuille":
    slow_writing("ciseau ! J'ai gagné.")

if answer1 == "ciseau":
    slow_writing("pierre ! J'ai gagné.")

time.sleep(1)
slow_writing("Je rigole.")
time.sleep(1)
slow_writing("Je vais désormais répondre aléatoirement selon ta réponse.\nTu auras donc toutes tes chances de gagner :)")
time.sleep(1)
slow_writing("On recommence.")
time.sleep(1.5)
slow_writing("Ready ?")
time.sleep(2)
slow_writing("3...")
time.sleep(1)
slow_writing("2...")
time.sleep(1)
slow_writing("1...")
time.sleep(1)
valid_answer = False
draw = True
want_to_continue = True
while not valid_answer and draw and want_to_continue:
    slow_writing("Tape ton choix au clavier, sans majuscule :")

    answer2 = input()

    if answer2 == "pierre" or answer2 == "feuille" or answer2 == "ciseau":
        valid_answer = True
        match random.randrange(1,3):
            case 1:
                computer_answer = "pierre"
            case 2:
                computer_answer = "feuille"
            case 3:
                computer_answer = "ciseau"
            case _:
                slow_writing("abord mission! not normal lol (should not happen)")
                exit(-1)
        result = result_duel(answer2,computer_answer)
        match result:
            case -1:
                slow_writing("Egalité ! On recommence ?")
            case 0:
                slow_writing("Tu as gagné ! On recommence ?")
            case 1:
                slow_writing("Tu as perdu ! On recommence ?")
        slow_writing("Tape OUI ou NON en majuscule.")
        answer_post_result = input()
        if answer_post_result == "OUI":
            want_to_continue = True
            valid_answer = False
        if answer_post_result == "NON":
            want_to_continue = False
            slow_writing("Ok, adieu et mange tes morts.")


    else:
        valid_answer = False
        slow_writing("Tu n'as le choix qu'entre pierre, feuille ou ciseau.\nEt puits n'existe pas.\nRecommence.")