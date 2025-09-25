from module import MetaData
from module import Description
import curses
from curses import wrapper
import time

heading = f""" 
  ___  _    _ _____     ___ _____  _____ _   _                 _             
 / _ \| |  | /  ___|   |_  /  ___||  _  | \ | |               | |            
/ /_\ \ |  | \ `--.      | \ `--. | | | |  \| |_ __ ___   __ _| | _____ _ __ 
|  _  | |/\| |`--. \     | |`--. \| | | | . ` | '_ ` _ \ / _` | |/ / _ \ '__|
| | | \  /\  /\__/ / /\__/ /\__/ /\ \_/ / |\  | | | | | | (_| |   <  __/ |   
\_| |_/\/  \/\____/  \____/\____/  \___/\_| \_/_| |_| |_|\__,_|_|\_\___|_|  \n"""

stateA = "<incomplete>"
stateB = "<complete>"
stateC = " <optional>"
stateD = " <required>"

formatStateOne = stateA
formatStateTwo = stateD
descriptionStateOne = stateA
descriptionStateTwo = stateD

def main (stdscr):
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    height, width = stdscr.getmaxyx()

   
    #stdscr.clear()
    #stdscr.addstr(heading, curses.color_pair(1))

    def progressBar():
            i = 0
            while i < width:
                stdscr.addstr("#", curses.color_pair(2))
                stdscr.refresh()
                i += 1
                time.sleep(0.02)
                if i == width:
                    return

    #progressBar()

    y = 0
    while True:
         
         key = stdscr.getkey()
         if key == "KEY_UP":
              y -= 1
         elif key == "KEY_DOWN":
              y += 1

         stdscr.clear()
         stdscr.addstr(y, ">", curses.A_BLINK)
         stdscr.refresh()

wrapper(main)



while True:
    text = f"Welcome to the AWS Cloud Formation JSONmaker! \nIf you would like a simple way to create basic template, type 'a' \nIf you want more control over your template, type 'b'"
    optionOne = input(text)
    if optionOne == "a":
        print("Guided Construction")
        break
    elif optionOne == "b":
        print("Advanced Construction")
        beginACon = f"Here are the 10 different options to configure to complete your template.\n 1: Format Version {formatStateOne}{formatStateTwo} \n 2: Description {descriptionStateOne}{descriptionStateTwo} \n 3: Metadata"
        aConstruction = input(beginACon)
        break
    else:
        print("Invalid option, please try again")






"""
queryDescription = input("To input any template description, type 'Description'")
if queryDescription == "Description":
    test1 = MetaData("JSON string", "")
    test1.queryUser()
"""

#Creating .json template to be modified by the program
templateText = """
{
  "AWSTemplateFormatVersion" : "version date",

  "Description" : "JSON string",

  "Metadata" : {
    template metadata
  },

  "Parameters" : {
    set of parameters
  },
  
  "Rules" : {
    set of rules
  },

  "Mappings" : {
    set of mappings
  },

  "Conditions" : {
    set of conditions
  },

  "Transform" : {
    set of transforms
  },

  "Resources" : {
    set of resources
  },
  
  "Outputs" : {
    set of outputs
  }
}
"""

#creating a .json file out of the template
f1 = open("CFtemp.json", "w")
f1.write(templateText)
f1.close()



"""
queryMetadata = input("To input any Template-level metadata, type 'Template Metadata'")
if queryMetadata == "Template Metadata":
    test1 = MetaData("template metadata", "")
    test1.queryUser()
"""