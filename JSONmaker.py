from module import OptionList
from module import AdvancedConstruction

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

#Creating .json template to be modified by the program
templateText = """s
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


while True:
    text = f"{WHITE}Welcome to the AWS Cloud Formation JSONmaker! \nIf you would like a simple way to create basic template, type 'a' \nIf you want more control over your template, type 'b'"
    optionOne = input(text)
    if optionOne == "a":
        print("Guided Construction")
        break
    elif optionOne == "b":
        aCon = False
        break
    else:
        print("Invalid option, please try again")

program = True

# Create the AdvancedConstruction instance once
advanced_construction = AdvancedConstruction()

while program == True:
  while aCon == False:
    aConstruction = input("please input the number of the option you would like to change:")
    aCon = True      

  while aCon == True:
      if aConstruction == "1":
          format1 = OptionList("version date", "", "format version", advanced_construction, 1)
          format1.queryUser()
          aCon = False
      elif aConstruction == "2":
          description1 = OptionList("JSON string", "", "description", advanced_construction, 2)
          description1.queryUser()
          aCon = False
      elif aConstruction == "3":
          metadata1 = OptionList("template metadata", "", "metadata", advanced_construction, 3)
          metadata1.queryUser()
          aCon = False
      elif aConstruction == "4":
          parameters1 = OptionList("set of parameters", "", "parameter", advanced_construction, 4)
          parameters1.queryUser()
          aCon = False
      elif aConstruction == "5":
          rules1 = OptionList("set of rules", "", "rules", advanced_construction, 5)
          rules1.queryUser()
          aCon = False
      elif aConstruction == "6":
          mappings1 = OptionList("set of mappings", "", "mappings", advanced_construction, 6)
          mappings1.queryUser()
          aCon = False
      elif aConstruction == "7":
          conditions1 = OptionList("set of conditions", "", "conditions", advanced_construction, 7)
          conditions1.queryUser()
          aCon = False        
      elif aConstruction == "8":
          transforms1 = OptionList("set of transforms", "", "transforms", advanced_construction, 8)
          transforms1.queryUser()
          aCon = False        
      elif aConstruction == "9":
          resources1 = OptionList("set of resources", "", "resources", advanced_construction, 9)
          resources1.queryUser()
          aCon = False         
      elif aConstruction == "10":
          outputs1 = OptionList("set of outputs", "", "outputs", advanced_construction, 10)
          outputs1.queryUser()
          aCon = False
      elif aConstruction == "exit":
        program = False
        aCon = False
      else:
        print("Invalid option, please try again")
        aCon = False
