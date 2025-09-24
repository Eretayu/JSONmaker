from module import MetaData
from module import Description

stateA = "<incomplete>"
stateB = "<complete>"
stateC = "<optional>"
stateD = "<required>"

formatState = stateA, stateD


while True:
    optionOne = input("Welcome to the AWS Cloud Formation wizard! \nIf you would like a simple way to create basic template, type 'a' \nIf you want more control over your template, type 'b'")
    if optionOne == "a":
        print("Guided Construction")
        break
    elif optionOne == "b":
        print("Advanced Construction")
        beginACon = f"There are 10 different options to configure to complete your template.\n 1: Format Version {formatState} \n 2: Description \n3: Metadata"
        aConstruction = input(beginACon)
        break
    else:
        print("Invalid option, please try again")


"""
queryDescription = input("To input any template description, type 'Description'")
if queryDescription == "Description":
    test1 = MetaData("JSON string", "")
    test1.queryUser()
    test1.declareState()
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