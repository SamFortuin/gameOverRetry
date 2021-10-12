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
        time.sleep(0.1)

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
  print_slow("You take the Condom with you.\n")
  condom = True
clearScreen(2)

print_slow(" \
You put on your jacket & backpack. \n \
You put on your shoes and tie your shoelaces. \n \
You open the door and go outside.\n \
You close the door behind you and start walking.\n") 
