from module import MetaData


def giveOptions():
    optionOne = input("Welcome to the AWS Cloud Formation wizard! \nIf you would like a simple way to create basic template, type 'a' \nIf you want more control over your template, type 'b'")
    if optionOne == "a":
        print("Guided Construction")
        with open(Guided.py, "r") as file:
            exec(file.read())
    elif optionOne == "b":
        print("Advanced Construction")

    else:
        print("Invalid option, please try again")
        giveOptions()



giveOptions()


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