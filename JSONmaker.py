from module import OptionList

ORANGE = '\033[38;5;208m'
WHITE =  '\033[0m'

heading = f""" {ORANGE}
  ___  _    _ _____     ___ _____  _____ _   _                 _             
 / _ \| |  | /  ___|   |_  /  ___||  _  | \ | |               | |            
/ /_\ \ |  | \ `--.      | \ `--. | | | |  \| |_ __ ___   __ _| | _____ _ __ 
|  _  | |/\| |`--. \     | |`--. \| | | | . ` | '_ ` _ \ / _` | |/ / _ \ '__|
| | | \  /\  /\__/ / /\__/ /\__/ /\ \_/ / |\  | | | | | | (_| |   <  __/ |   
\_| |_/\/  \/\____/  \____/\____/  \___/\_| \_/_| |_| |_|\__,_|_|\_\___|_|  \n"""

print(heading)

stateA = "<incomplete>"
stateB = "<complete>"
stateC = " <optional>"
stateD = " <required>"

formatStateOne = stateA
formatStateTwo = stateD
descriptionStateOne = stateA
descriptionStateTwo = stateD

while True:
    text = f"{WHITE}Welcome to the AWS Cloud Formation JSONmaker! \nIf you would like a simple way to create basic template, type 'a' \nIf you want more control over your template, type 'b'"
    optionOne = input(text)
    if optionOne == "a":
        print("Guided Construction")
        break
    elif optionOne == "b":
        print(f"Here are the 10 different options to configure to complete your template.\n 1: Format Version {formatStateOne}{formatStateTwo} \n 2: Description {descriptionStateOne}{descriptionStateTwo} \n 3: Metadata")
        aConstruction = input("please input the number of the option you would like to change:")
        break
    else:
        print("Invalid option, please try again")

while True:
    if aConstruction == "1":
        pass
    elif aConstruction == "2":
        description1 = OptionList("JSON string", "", "description")
        description1.queryUser()
        break
    elif aConstruction == "3":
        metadata1 = OptionList("template metadata", "", "metadata")
        metadata1.queryUser()
        break
    elif aConstruction == "4":
        pass
    elif aConstruction == "5":
        pass
    elif aConstruction == "6":
        pass
    elif aConstruction == "7":
        pass
    elif aConstruction == "8":
        pass
    elif aConstruction == "9":
        pass
    elif aConstruction == "10":
        pass
    else:
        print("Invalid option, please try again")
        break




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


