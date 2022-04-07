from yournumber import *
from colorama import Fore,Style

#השוואה בין המספרים שלי ללוטו

counter = 0
countgold = 0
for number in powerballnumbers[:5]:
    if number in mynumber[:5]:
        counter += 1
if powerballnumbers[-1] == mynumber[-1]:
    countgold += 1

    if mynumber == powerballnumbers:
        print("you won the Jackpot $324,000,000")
# לללא מספר חזק
    if counter == 5 and countgold == 1:
        print("you won $1,000,000")
# #עם מספר חזק
    elif counter == 4 and countgold == 1:
        print(" you won $10,000")
# ללא מספר חזק
    elif counter == 4 and countgold == 0:
        print(" you won $100")
#עם מספר חזק
    elif counter == 3 and countgold == 1:
        print("you won $100")
#ללא מספר חזק
    elif counter == 3 and countgold == 0:
        print("you won $7")
#עם מספר חזק
    elif counter == 2 and countgold == 1:
        print("you won $7")
#עם מספר חזק
    elif counter == 1 and countgold == 1:
        print("you won $4")
#עם מספר חזק
    elif counter == 0 and countgold == 1:
            print("you won $4")
    else:
        print("Try agine")

print("you guessed"+ " " + str(counter)+" "+"numbers correct")
print(Fore.GREEN,f'{counter}',Style.RESET_ALL)