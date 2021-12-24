# Mert Erciyas 99058235
from time import sleep
from os import system
from sys import stdout

# Dating Simulator
# Goal: Try to find your loved one
def clearScreen(sleepTime):
    sleep(sleepTime)
    system("cls")

def printSlow(str,interval=0.005): #prints slow and removes the screen
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(interval)

def endingScreen(num):
  endingLine1 = {1:'  __     ________ ',2:'  ___      ________ ',3:'  ____     ________ ',4:'  _  _     ________ ',5:'  _____    ________ ',6:'    __     ________ ',7:'  ______ ________ '}
  endingLine2 = {1:' /_ |   / /____  |',2:' |__ \    / /____  |',3:' |___ \   / /____  |',4:' | || |   / /____  |',5:' | ____|  / /____  |',6:'   / /    / /____  |',7:' |____  / /____  |'}
  endingLine3 = {1:'  | |  / /    / / ',2:'    ) |  / /    / / ',3:'   __) | / /    / / ',4:' | || |_ / /    / / ',5:' | |__   / /    / / ',6:'  / /_   / /    / / ',7:'     / / /    / / '}
  endingLine4 = {1:'  | | / /    / /  ',2:'   / /  / /    / /  ',3:'  |__ < / /    / /  ',4:' |__   _/ /    / /  ',5:' |___ \ / /    / /  ',6:" | '_ \ / /    / /  ",7:'    / / /    / /  '}
  endingLine5 = {1:'  | |/ /    / /   ',2:'  / /_ / /    / /   ',3:'  ___) / /    / /   ',4:'    | |/ /    / /   ',5:'  ___) / /    / /   ',6:' | (_) / /    / /   ',7:'   / / /    / /   '}
  endingLine6 = {1:'  |_/_/    /_/    ',2:' |____/_/    /_/    ',3:' |____/_/    /_/    ',4:'    |_/_/    /_/    ',5:' |____/_/    /_/    ',6:'  \___/_/    /_/    ',7:'  /_/_/    /_/    '}
  print(f" \
        ______           _ _             {endingLine1[num]} \n\
        |  ____|         | (_)            {endingLine2[num]}\n\
        | |__   _ __   __| |_ _ __   __ _ {endingLine3[num]}\n\
        |  __| | '_ \ / _` | | '_ \ / _` |{endingLine4[num]}\n\
        | |____| | | | (_| | | | | | (_| |{endingLine5[num]}\n\
        |______|_| |_|\__,_|_|_| |_|\__, |{endingLine6[num]}\n\
                                     __/ |\n\
                                    |___/")
               
# Variable 
#TODO change true and falses into list/dict
nintendoSwitch, comicBook, condom, girl1, classMate, snickers, crackers, goClass, leaveClass = False
#old vars
# comicBook = False
# condom = False
# girl1 = False
# classMate = False
# snickers = False
# crackers = False
# goClass = False
# leaveClass = False

clearScreen(0)
print("\
                                                 ******       ****** \n\
                                               **********   ********** \n\
                                             ************* ************* \n\
                                            ***************************** \n\
                                            ***************************** \n\
                                            ***************************** \n\
                                             *************************** \n\
                                               *********************** \n\
                                                 ******************* \n\
                                                   *************** \n\
                                                     *********** \n\
                                                       ******* \n\
                                                         *** \n\
                                                          * \n\
 ____              __                            ____                             ___             __                    \n\
/\  _`\           /\ \__  __                    /\  _`\   __                     /\_ \           /\ \__                 \n\
\ \ \/\ \     __  \ \ ,_\/\_\    ___      __    \ \,\L\_\/\_\    ___ ___   __  __\//\ \      __  \ \ ,_\   ___   _ __   \n\
 \ \ \ \ \  /'__`\ \ \ \/\/\ \ /' _ `\  /'_ `\   \/_\__ \|/\ \ /' __` __`\/\ \/\ \ \ \ \   /'__`\ \ \ \/  / __`\/\`'__\ \n\
  \ \ \_\ \/\ \L\.\_\ \ \_\ \ \/\ \/\ \/\ \L\ \    /\ \L\ \ \ \/\ \/\ \/\ \ \ \_\ \ \_\ \_/\ \L\.\_\ \ \_/\ \L\ \ \ \/  \n\
   \ \____/\ \__/.\_|\ \__|\ \_\ \_\ \_\ \____ \   \ `\____\ \_\ \_\ \_\ \_\ \____/ /\____\ \__/.\_\| \__\ \____/\ \_\  \n\
    \/___/  \/__/\/_/ \/__/ \/_/\/_/\/_/\/___L\ \   \/_____/\/_/\/_/\/_/\/_/\/___/  \/____/\/__/\/_/ \/__/\/___/  \/_/  \n\
                                          /\____/                                                                       \n\
                                          \_/__/                                                                        \n\
                         _____ _       _                       _               _                                        \n\
                        |   __|_|___ _| |   _ _ ___ _ _ ___   | |___ _ _ ___ _| |   ___ ___ ___  \n\
                        |   __| |   | . |  | | | . | | |  _|  | | . | | | -_| . |  | . |   | -_| \n\
                        |__|  |_|_|_|___|  |_  |___|___|_|    |_|___|\_/|___|___|  |___|_|_|___| \n\
                                           |___|                                                 \n\
")

clearScreen(3)

# House segment

printSlow("Your adventure starts in your room.\n\
You wake up, and prepare for school.\n\
What do you do first?\n\
• Clean your face.\n\
• Dont clean your face\n\
What do you do?\n")
cleanFace = input('').lower()[:3] #empty input because question text is printed slow
if cleanFace == "cle":
  printSlow("Goodjob. You cleaned your face.")
  cleanFace = True
elif cleanFace == "don":
  printSlow("You decided not to clean your face")
  cleanFace = False
#TODO function that repeats instead of exiting program
# else: 
#   print("invalid input, exiting program")
#   exit()
clearScreen(2)

#TODO replace with single printSlow
printSlow("You start going downstairs.\n\
You fill your bag with stuff that you need for school.\n\
What else do you take with you?\n\
• Nintendo Switch\n\
• Comic Book\n\
• Condoms\n\
What do you take with you?\n")
bag = input('').lower()[:5]
if bag == "ninte" or bag == 'switc':
  printSlow("You put the Nintendo Switch in your bag.\n")
  nintendoSwitch = True
elif bag == "comic":
  printSlow("You put the Comic Book in your bag\n")
  comicBook = True
elif bag == 'condo':
  printSlow("You take the Condoms with you.\n")
  condom = True
clearScreen(2)

printSlow("You put on your jacket & backpack. \n\
You put on your shoes and tie your shoelaces. \n\
You open the door and go outside.\n\
You close the door behind you and start walking.\n\
You see a girl from school. \n\
Do you go with her or without her? \n\
• With\n\
• Without\n")
soloDuo = input("What do you do?\n").lower().replace(" ","")
if soloDuo == "with":
  printSlow("You decided to go with the girl. \n")
  girl1 = True
elif soloDuo == "without":
  printSlow("You decided not to go with the girl.\n")
  girl1 = False
# else:
#   printSlow("invalid input, exiting program")
#   exit()
clearScreen(2)

print("\
   _      __                                  ___             __                    \n\
 /' \    /\ \                                /\_ \           /\ \__                 \n\
/\_, \   \ \ \___     ___   __  __  _ __     \//\ \      __  \ \ ,_\    __   _ __   \n\
\/_/\ \   \ \  _ `\  / __`\/\ \/\ \/\`'__\     \ \ \   /'__`\ \ \ \/  /'__`\/\`'__\ \n\
   \ \ \   \ \ \ \ \/\ \L\ \ \ \_\ \ \ \/       \_\ \_/\ \L\.\_\ \ \_/\  __/\ \ \/  \n\
    \ \_\   \ \_\ \_\ \____/\ \____/\ \_\       /\____\ \__/.\_|\ \__\ \____|\ \_\  \n\
     \/_/    \/_/\/_/\/___/  \/___/  \/_/       \/____/\/__/\/_/ \/__/\/____/ \/_/  \n")
clearScreen(2)
# School segment

if girl1 == True:
  #TODO turn into single statement
  printSlow("You and the girl walk together to school.\nYou walk into the school and wave goodbye to the girl.")
else:
  #TODO single statement
  printSlow('You walk to school by yourself.\nYou enter school and head to class\n')
printSlow("You walk into your class.\n")
printSlow(" \
You enter the class.\n\
You take a seat and proceed to go further in your class\n")
clearScreen(2)

if girl1 == True:
  if nintendoSwitch == True:
    printSlow("The girl says: Hey I see that you have a Nintendo Switch I would love if I could play with it.\n")
    printSlow("You and the girl play together with the switch.\n")
    endingScreen(1)
    exit()
  elif comicBook == True:
    printSlow("The girl says: Hey i see that you have a Comic Book can i take a look at it?\n")
    printSlow("She takes a look in the comic and finds out its about Spiderman.\n")
    printSlow("You and the girl sit with eachother and read the comic together\n")
    endingScreen(2)
    exit()
  else:
    printSlow("She sees the Condoms.\n")
    printSlow("The girl says: Eww disgusting.\n")
    printSlow("Then she runs away\n")
    printSlow("And now you're sad.\n")
    endingScreen(3)
    exit()
else:
  printSlow("You leave class alone and head to the cafetaria.\n")
  printSlow("You see some class mates.\n")
  printSlow("Do you sit with them?\n")
  printSlow("• Yes\n")
  printSlow("• No\n")
  classMate = input("What do you do?\n")
  classMate = classMate.lower()
clearScreen(2)
if classMate == "yes":
  printSlow("You decide to sit next to your classmates.\n")
  printSlow("You sit next to the girl you saw in the morning.\n")
  printSlow("she asked why did you not go with her.\n")
  printSlow("• Lie\n")
  printSlow("• Truth\n")
  girlLie = input("What do you do?\n")
  girlLie = girlLie.lower()
  if girlLie == "lie":
    printSlow("You tell her that you already have a girlfriend.\n")
    printSlow("the girl becomes confused and walks away.\n")
    endingScreen(4)
    exit()
  else:
    printSlow("You decide to tell her the truth\n")
    printSlow("You tell her that you're to nervous to talk with girls.\n")
    printSlow("then you start running away in fear.\n")
    endingScreen(5)
    exit()                            
else:
  printSlow("You decide to sit alone.\n")
  printSlow("you pull out your lunch pack\n")
  printSlow("You pull out a Snicker bar and some Crackers\n")
  printSlow("Which one do you take first?\n")
  printSlow("• Snickers\n")
  printSlow("• Crackers\n")
  lunch = input("What do you choose?\n")
  lunch = lunch.lower()
  
  if lunch == "snickers":
    printSlow("You ate the Snickers first.\n")
    snickers = True
  elif lunch == "crackers":
    printSlow("You ate the Crackers first.\n")
    crackers = True
  else:
    printSlow("You decided not to eat anything.\n")
    printSlow("You died of hunger\n")
    endingScreen(6)
    exit()
clearScreen(2)

printSlow("You leave the cafateria.\n\
You see that you have another class.\n\
Do you skip class or go to class?\n\
• Go to class\n\
• Skip class\n\
What do you do?\n")
skipClass = input("").lower().replace(' ','')[:4]

if skipClass == "goto":
  goClass = True
  printSlow("You decide to go to class.\n")
else:
  leaveClass = True
  printSlow("You decide to leave the class.\n") 
clearScreen(2)

if goClass == True:
  printSlow("You decide to go to class.\nYou enter the class.\nYou see your teacher Bouwman come close to you.\nhe says: Meet me after class\n")
  print("\
    _______ _            _______                ______           _ _             \n\
   |__   __| |          |__   __|              |  ____|         | (_)            \n\
      | |  | |__   ___     | |_ __ _   _  ___  | |__   _ __   __| |_ _ __   __ _ \n\
      | |  | '_ \ / _ \    | | '__| | | |/ _ \ |  __| | '_ \ / _` | | '_ \ / _` |\n\
      | |  | | | |  __/    | | |  | |_| |  __/ | |____| | | | (_| | | | | | (_| |\n\
      |_|  |_| |_|\___|    |_|_|   \__,_|\___| |______|_| |_|\__,_|_|_| |_|\__, |\n\
                                                                            __/ |\n\
                                                                           |___/ ")
  exit()
else:
  printSlow("You decide to skip class.\nAnd you remindend yourself that you will be forever alone.\n")
  endingScreen(7)
exit()
