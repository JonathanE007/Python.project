
class Powerball:

    def __init__(self,name,color):
        self.name = name
        self.color = color


from colorama import Fore,Style




import random


#המספרים של הלוטו היומי
print("Today's Powerball Winning Numbers:")
powerballnumbers = []
for i in range(0,5):
    number = random.randint(1,20)

    while number in powerballnumbers:
        number = random.randint(1,20)
    powerballnumbers.append(number)

powerballnumbers.sort()

# מספר 6 זהב
goldnumber = random.randint(1,10)
powerballnumbers.append({goldnumber})
print(Fore.BLUE,f'{powerballnumbers[:5]}',Style.RESET_ALL,Fore.YELLOW,f'{powerballnumbers[-1]}',Style.RESET_ALL)


