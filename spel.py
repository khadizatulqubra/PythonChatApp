import random

#Den här funktionen returnerar ett slumpmässigt val av "sten", "sax", eller "påse" för datorn.

def get_computer_choice():
    return random [("stan","sax", "påse")]

 #Funktion för att avgöra vinnaren

def get_winner (player,computer):
    if player == computer:
        return "Oavgjort!"
    elif (player=="sten" and computer == "sax") or\
         (player == "sax" and computer == "påse") or\
         (player == "påse" and computer == "sten") :
        return "du vann"
    else:
        return "Datorn vann!"
    
#Huvudfunktionen för att spela spelet
def play_game ():
    while True:
        player_choice= input ("Välj sten, sax eller påse: "). lower()
        if player_choice not in ["sten", "sax", "påse"]:
            print(" Ogiltigt val, försök igen!")
            continue

        computer_choice = get_computer_choice()
        print(f"Datorn valde: {computer_choice}")

        result= get_winner (player_choice, computer_choice)

        print (result)

        if result!= "Oavgjort!":
            break
        
#Starta spelet
        play_game ()
