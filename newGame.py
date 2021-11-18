# Mert Erciyas 99058235
import time, os, sys

# Dating Simulator
# Goal: Try to find your loved one
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")
# Prints slow and removes the screen
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0005)
# Variable 
nintendoSwitch = False
comicBook = False
condom = False
girl1 = False
classMate = False
snickers = False
crackers = False
goClass = False
leaveClass = False
clearScreen(1)

print(" \
                                                 ******       ****** \n \
                                               **********   ********** \n \
                                             ************* ************* \n \
                                            ***************************** \n \
                                            ***************************** \n \
                                            ***************************** \n \
                                             *************************** \n \
                                               *********************** \n \
                                                 ******************* \n \
                                                   *************** \n \
                                                     *********** \n \
                                                       ******* \n \
                                                         *** \n \
                                                          * \n \
 ____              __                            ____                             ___             __                    \n \
/\  _`\           /\ \__  __                    /\  _`\   __                     /\_ \           /\ \__                 \n \
\ \ \/\ \     __  \ \ ,_\/\_\    ___      __    \ \,\L\_\/\_\    ___ ___   __  __\//\ \      __  \ \ ,_\   ___   _ __   \n \
 \ \ \ \ \  /'__`\ \ \ \/\/\ \ /' _ `\  /'_ `\   \/_\__ \|/\ \ /' __` __`\/\ \/\ \ \ \ \   /'__`\ \ \ \/  / __`\/\`'__\ \n \
  \ \ \_\ \/\ \L\.\_\ \ \_\ \ \/\ \/\ \/\ \L\ \    /\ \L\ \ \ \/\ \/\ \/\ \ \ \_\ \ \_\ \_/\ \L\.\_\ \ \_/\ \L\ \ \ \/  \n \
   \ \____/\ \__/.\_|\ \__|\ \_\ \_\ \_\ \____ \   \ `\____\ \_\ \_\ \_\ \_\ \____/ /\____\ \__/.\_\| \__\ \____/\ \_\  \n \
    \/___/  \/__/\/_/ \/__/ \/_/\/_/\/_/\/___L\ \   \/_____/\/_/\/_/\/_/\/_/\/___/  \/____/\/__/\/_/ \/__/\/___/  \/_/  \n \
                                          /\____/                                                                       \n \
                                          \_/__/                                                                        \n \
                         _____ _       _                       _               _                                                                \n \
                        |   __|_|___ _| |   _ _ ___ _ _ ___   | |___ _ _ ___ _| |   ___ ___ ___  \n \
                        |   __| |   | . |  | | | . | | |  _|  | | . | | | -_| . |  | . |   | -_| \n \
                        |__|  |_|_|_|___|  |_  |___|___|_|    |_|___|\_/|___|___|  |___|_|_|___| \n \
                                           |___|                                                 \n \
")

clearScreen(3)

# House segment

print_slow("Your adventure starts in your room.\n")
print_slow("You wake up, and prepare for school.\n")
print_slow("what do you do first?\n")
print_slow("• Clean your face.\n")
print_slow("• Dont clean your face\n")
cleanFace = input("What do you do?\n")
cleanFace = cleanFace.lower().replace(" ","").replace("'","")
if cleanFace == "cleanyourface":
  print_slow("Goodjob. You cleaned your face.\n")
  cleanFace = True
elif "dont" in cleanFace:
  print_slow("You decided not to clean your face\n")
  cleanFace = False
else: 
  print("invalid input, exiting program")
  exit()
clearScreen(2)

print_slow("You start going downstairs.\n")
print_slow("You fill your bag with stuff that you need for school.\n")
print_slow("What else do you take with you?\n")
print_slow("• Nintendo Switch\n")
print_slow("• Comic Book\n")
print_slow("• Condoms\n")
bag = input("What do you take with you?\n")
bag = bag.lower().replace(" ","")
if bag == "nintendoswitch":
  print_slow("You put the Nintendo Switch in your bag.\n")
  nintendoSwitch = True
elif bag == "comicbook":
  print_slow("You put the Comic Book in your bag\n")
  comicBook = True
else:
  print_slow("You take the Condoms with you.\n")
  condom = True
clearScreen(2)

print_slow(" \
You put on your jacket & backpack. \n \
You put on your shoes and tie your shoelaces. \n \
You open the door and go outside.\n \
You close the door behind you and start walking.\n \
You see a girl from school. \n \
Do you go with her or without her? \n \
• With \n \
• Without \n") 
soloDuo = input("What do you do?\n")
soloDuo = soloDuo.lower().replace(" ","")
if soloDuo == "with":
  print_slow("You decided to go with the girl. \n")
  girl1 = True
elif soloDuo == "without":
  print_slow("You decided not to go with the girl.\n")
  girl1 = False
else:
  print_slow("invalid input, exiting program")
  exit()
clearScreen(2)

print(" \
   _      __                                  ___             __                    \n \
 /' \    /\ \                                /\_ \           /\ \__                 \n \
/\_, \   \ \ \___     ___   __  __  _ __     \//\ \      __  \ \ ,_\    __   _ __   \n \
\/_/\ \   \ \  _ `\  / __`\/\ \/\ \/\`'__\     \ \ \   /'__`\ \ \ \/  /'__`\/\`'__\ \n \
   \ \ \   \ \ \ \ \/\ \L\ \ \ \_\ \ \ \/       \_\ \_/\ \L\.\_\ \ \_/\  __/\ \ \/  \n \
    \ \_\   \ \_\ \_\ \____/\ \____/\ \_\       /\____\ \__/.\_|\ \__\ \____|\ \_\  \n \
     \/_/    \/_/\/_/\/___/  \/___/  \/_/       \/____/\/__/\/_/ \/__/\/____/ \/_/  \n \
                                                                                   \n \
  ")
clearScreen(2)
# School segment

if girl1 == True:
  print_slow("You and the girl walk together to school.\n")
  print_slow("You walk into the school and wave goodbye to the girl.\n")
else:
  print_slow("You walked alone to school.\n")
  print_slow("You walk into the school alone.\n")
print_slow("You walk into your class.\n")

print_slow(" \
You enter the class.\n \
You take a seat and proceed to go further in your class\n")
clearScreen(2)

if girl1 == True:
  if nintendoSwitch == True:
    print_slow("The girl says: Hey I see that you have a Nintendo Switch I would love if I could play with it.\n")
    print_slow("You and the girl play together with the switch.\n")
    print(" \
       ______           _ _               __     ________ \n \
      |  ____|         | (_)             /_ |   / /____  |\n \
      | |__   _ __   __| |_ _ __   __ _   | |  / /    / / \n \
      |  __| | '_ \ / _` | | '_ \ / _` |  | | / /    / /  \n \
      | |____| | | | (_| | | | | | (_| |  | |/ /    / /   \n \
      |______|_| |_|\__,_|_|_| |_|\__, |  |_/_/    /_/    \n \
                                    _/ |                 \n \
                                  |___/                   ")
    exit()
  elif comicBook == True:
    print_slow("The girl says: Hey i see that you have a Comic Book can i take a look at it?\n")
    print_slow("She takes a look in the comic and finds out its about Spiderman.\n")
    print_slow("You and the girl sit with eachother and read the comic together\n")
    print(" \
       ______           _ _               ___      ________ \n \
      |  ____|         | (_)             |__ \    / /____  | \n \
      | |__   _ __   __| |_ _ __   __ _     ) |  / /    / / \n \
      |  __| | '_ \ / _` | | '_ \ / _` |   / /  / /    / /  \n \
      | |____| | | | (_| | | | | | (_| |  / /_ / /    / /   \n \
      |______|_| |_|\__,_|_|_| |_|\__, | |____/_/    /_/    \n \
                                   __/ |                    \n \
                                  |___/                     ")
    exit()
  else:
    print_slow("She sees the Condoms.\n")
    print_slow("The girl says: Eww disgusting.\n")
    print_slow("Then she runs away\n")
    print_slow("And now you're sad.\n")
    print(" \
         ______           _ _               ____     ________ \n \
        |  ____|         | (_)             |___ \   / /____  |\n \
        | |__   _ __   __| |_ _ __   __ _    __) | / /    / / \n \
        |  __| | '_ \ / _` | | '_ \ / _` |  |__ < / /    / /  \n \
        | |____| | | | (_| | | | | | (_| |  ___) / /    / /   \n \
        |______|_| |_|\__,_|_|_| |_|\__, | |____/_/    /_/    \n \
                                     __/ |                    \n \
                                    |___/                    ")
    exit()
else:
  print_slow("You leave class alone and head to the cafetaria.\n")
  print_slow("You see some class mates.\n")
  print_slow("Do you sit with them?\n")
  print_slow("• Yes\n")
  print_slow("• No\n")
  classMate = input("What do you do?\n")
  classMate = classMate.lower()
clearScreen(2)
if classMate == "yes":
  print_slow("You decide to sit next to your classmates.\n")
  print_slow("You sit next to the girl you saw in the morning.\n")
  print_slow("she asked why did you not go with her.\n")
  print_slow("• Lie\n")
  print_slow("• Truth\n")
  girlLie = input("What do you do?\n")
  girlLie = girlLie.lower()
  if girlLie == "lie":
    print_slow("You tell her that you already have a girlfriend.\n")
    print_slow("the girl becomes confused and walks away.\n")
    print(" \
       ______           _ _               _  _     ________ \n \
      |  ____|         | (_)             | || |   / /____  | \n \
      | |__   _ __   __| |_ _ __   __ _  | || |_ / /    / /  \n \
      |  __| | '_ \ / _` | | '_ \ / _` | |__   _/ /    / /  \n \
      | |____| | | | (_| | | | | | (_| |    | |/ /    / /   \n \
      |______|_| |_|\__,_|_|_| |_|\__, |    |_/_/    /_/    \n \
                                   __/ |                    \n \
                                  |___/                    ")
    exit()
  else:
    print_slow("You decide to tell her the truth\n")
    print_slow("You tell her that you're to nervous to talk with girls.\n")
    print_slow("then you start running away in fear.\n")
    print(" \
       ______           _ _               _____    ________ \n \
      |  ____|         | (_)             | ____|  / /____  | \n \
      | |__   _ __   __| |_ _ __   __ _  | |__   / /    / /  \n \
      |  __| | '_ \ / _` | | '_ \ / _` | |___ \ / /    / /   \n \
      | |____| | | | (_| | | | | | (_| |  ___) / /    / /    \n \
      |______|_| |_|\__,_|_|_| |_|\__, | |____/_/    /_/    \n \
                                   __/ |                    \n \
                                  |___/                     ")
    exit()                            
else:
  print_slow("You decide to sit alone.\n")
  print_slow("you pull out your lunch pack\n")
  print_slow("You pull out a Snicker bar and some Crackers\n")
  print_slow("Which one do you take first?\n")
  print_slow("• Snickers\n")
  print_slow("• Crackers\n")
  lunch = input("What do you choose?\n")
  lunch = lunch.lower()
  
  if lunch == "snickers":
    print_slow("You ate the Snickers first.\n")
    snickers = True
  elif lunch == "crackers":
    print_slow("You ate the Crackers first.\n")
    crackers = True
  else:
    print_slow("You decided not to eat anything.\n")
    print_slow("You died of hunger\n")
    print(" \
       ______           _ _                 __     ________ \n \
      |  ____|         | (_)               / /    / /____  | \n \
      | |__   _ __   __| |_ _ __   __ _   / /_   / /    / / \n \
      |  __| | '_ \ / _` | | '_ \ / _` | | '_ \ / /    / /  \n \
      | |____| | | | (_| | | | | | (_| | | (_) / /    / /   \n \
      |______|_| |_|\__,_|_|_| |_|\__, |  \___/_/    /_/    \n \
                                   __/ |                    \n \
                                  |___/                      ")
    exit()
clearScreen(2)

print_slow("You leave the cafateria.\n")
print_slow("You see that you have another class.\n")
print_slow("Do you skip class or go to class?\n")
print_slow("• Go to class\n")
print_slow("• Skip class\n")
skipClass = input("What do you do?\n")
skipClass = skipClass.lower()

if skipClass == "go to class":
  goClass = True
  print_slow("You decide to go to class.\n")
else:
  leaveClass = True
  print_slow("You decide to leave the class.\n") 
clearScreen(2)

if goClass == True:
  print_slow("You decide to go to class.\n")
  print_slow("You enter the class.\n")
  print_slow("You see your teacher Bouwman come close to you.\n")
  print_slow("he says: Meet me after class ;)\n")
  print(" \
    _______ _            _______                ______           _ _             \n \
   |__   __| |          |__   __|              |  ____|         | (_)            \n \
      | |  | |__   ___     | |_ __ _   _  ___  | |__   _ __   __| |_ _ __   __ _ \n \
      | |  | '_ \ / _ \    | | '__| | | |/ _ \ |  __| | '_ \ / _` | | '_ \ / _` |\n \
      | |  | | | |  __/    | | |  | |_| |  __/ | |____| | | | (_| | | | | | (_| |\n \
      |_|  |_| |_|\___|    |_|_|   \__,_|\___| |______|_| |_|\__,_|_|_| |_|\__, |\n \
                                                                            __/ |\n \
                                                                           |___/ ")
  exit()
else:
  print_slow("You decide to skip class.\n")
  print_slow("And you remindend yourself that you will be forever alone.\n")
  print(" \
     ______           _ _               ______ ________\n \
    |  ____|         | (_)             |____  / /____  | \n \
    | |__   _ __   __| |_ _ __   __ _      / / /    / /  \n \
    |  __| | '_ \ / _` | | '_ \ / _` |    / / /    / /  \n \
    | |____| | | | (_| | | | | | (_| |   / / /    / /   \n \
    |______|_| |_|\__,_|_|_| |_|\__, |  /_/_/    /_/    \n \
                                 __/ |                  \n \
                                |___/                   ")
exit()
