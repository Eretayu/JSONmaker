from module import OptionList
from module import AdvancedConstruction
from module import CheckTemplate
from module import Export

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
templateText = """
{
  "AWSTemplateFormatVersion" : "BLANK(1)",

  "Description" : "BLANK(2)",

  "Metadata" : {
    BLANK(3)
  },

  "Parameters" : {
    BLANK(4)
  },
  
  "Rules" : {
    BLANK(5)
  },

  "Mappings" : {
    BLANK(6)
  },

  "Conditions" : {
    BLANK(7)
  },

  "Transform" : {
    BLANK(8)
  },

  "Resources" : {
    BLANK(9)
  },
  
  "Outputs" : {
    BLANK(0)
  }
}
"""

#creating a .json file out of the template
f1 = open("CFtemp.json", "w")
f1.write(templateText)
f1.close()


text = f"{WHITE}Welcome to the AWS Cloud Formation JSONmaker!"

aCon = False
program = True
print(text)
# Create the AdvancedConstruction instance once
advanced_construction = AdvancedConstruction()



while program == True:
  while aCon == False:
    aConstruction = input("please input the number of the option you would like to change. Type 'done' when your template is complete, or 'exit' if you want to exit the program'.")
    aCon = True      

  while aCon == True:
      if aConstruction == "1":
          format1 = OptionList("BLANK(1)", "", "format version", advanced_construction, 1)
          format1.queryUser()
          aCon = False
      elif aConstruction == "2":
          description1 = OptionList("BLANK(2)", "", "description", advanced_construction, 2)
          description1.queryUser()
          aCon = False
      elif aConstruction == "3":
          metadata1 = OptionList("BLANK(3)", "", "metadata", advanced_construction, 3)
          metadata1.queryUser()
          aCon = False
      elif aConstruction == "4":
          parameters1 = OptionList("BLANK(4)", "", "parameter", advanced_construction, 4)
          parameters1.queryUser()
          aCon = False
      elif aConstruction == "5":
          rules1 = OptionList("BLANK(5)", "", "rules", advanced_construction, 5)
          rules1.queryUser()
          aCon = False
      elif aConstruction == "6":
          mappings1 = OptionList("BLANK(6)", "", "mappings", advanced_construction, 6)
          mappings1.queryUser()
          aCon = False
      elif aConstruction == "7":
          conditions1 = OptionList("BLANK(7)", "", "conditions", advanced_construction, 7)
          conditions1.queryUser()
          aCon = False        
      elif aConstruction == "8":
          transforms1 = OptionList("BLANK(8)", "", "transforms", advanced_construction, 8)
          transforms1.queryUser()
          aCon = False        
      elif aConstruction == "9":
          resources1 = OptionList("BLANK(9)", "", "resources", advanced_construction, 9)
          resources1.queryUser()
          aCon = False         
      elif aConstruction == "10":
          outputs1 = OptionList("BLANK(0)", "", "outputs", advanced_construction, 10)
          outputs1.queryUser()
          aCon = False
      elif aConstruction == "exit":
        program = False
        aCon = False
      elif aConstruction == "done":
          check = CheckTemplate()
          check.QueryUser()
          response = check.get_response()
          if response == "continue":
            aCon = False
            advanced_construction = AdvancedConstruction()
          elif response == "exit":
            export = Export()
            program = False
            aCon = False

      else:
        print("Invalid option, please try again")
        aCon = False

