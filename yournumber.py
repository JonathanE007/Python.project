from powerball import *
from colorama import Fore,Style


# המספרים שאני שמתי בלוטו
print("Your lucky numbers:")
mynumber = []
for i in range(0,5):
    number = random.randint(1,20)

    while number in mynumber:
        number = random.randint(1,20)

    mynumber.append(number)
mynumber.sort()
#מספר 6 זהב
goldnumber = random.randint(1,10)
mynumber.append({goldnumber})
(print(Fore.BLUE,f'{mynumber[:5]}',Style.RESET_ALL,Fore.YELLOW,f'{mynumber[-1]}',Style.RESET_ALL))


