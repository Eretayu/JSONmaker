from module import MetaData

from module import Description
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