from module import MetaData

def giveOptions():
    print("If you would like a simple way to create basic Cloud Formation template, type 'Guided Construction' if you want more control over your template, type 'Advanced Construction'")

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



begin = input("Welcome to the AWS Cloud Formation wizard! \nTo begin the program, pless type 'continue'. \nType anything else to quit the program.\n")
if begin == "continue":
    queryMetadata = input("To input any Template-level metadata, type 'Template Metadata'")
else:
    quit

if queryMetadata == "Template Metadata":
    test1 = MetaData("template metadata", "")
    test1.queryUser()