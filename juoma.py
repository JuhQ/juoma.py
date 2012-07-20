# This is a simple drinking game. Juoma means "a drink" in Finnish.
# Rules are simple:
# - List players
# - List available drinks
# - The person with the highest number has to drink the drink provided by the game, player can decide portion size
# - If you puke or pass out, you lose
# - If a drink runs out, it must be removed from the drink list
# - Last one who's not thrown up or passed out, IS THE WINNER!
# - Do not die
# - Have fun
# 
#  Juha Tauriainen @juha_tauriainen juha@bin.fi



# list players here
players = ["Juha", "Pekka", "Timo", "Liisa", "Maija"];

# list drinks here
drinks = ["Beer", "Koskenkorva", "Whiskey", "Milk"];

from random import randint

winnerString = ""
winner = 0

for player in players:
    roll = randint(0,100)
    
    string = "{0} rolls {1} for drink {2}".format(player, roll, drinks[randint(0, len(drinks) - 1)])
    print(string)
    if roll > winner:
        winner = roll
        winnerString = string

print("WINNER: {0}".format(winnerString))