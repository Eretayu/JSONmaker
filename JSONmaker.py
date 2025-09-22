
#Creating .json template to be modified by the program
templateText = """
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation Template for a simple web application",
    "Resources": {
        "EC2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "InstanceType": "t2.micro",
                "ImageId": "XXXXXXXXXXXXXXXXXXXXX",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "MyWebServer"
                    }
                ]
            }
        }
    }
}
"""

#creating a .json file out of the template
f1 = open("CFtemp.json", "w")
f1.write(templateText)
f1.close()

#create variables of different terms in the template that the user will replace.
textToSearchImageID = "XXXXXXXXXXXXXXXXXXXXX"
textToSearchInstanceName = "MyWebServer"
textToSearchInstanceType = "t2.micro"

#each of these functions replace one of the terms declared above with a user input response.
def instanceTypeChange():
    with open("CFtemp.json", "r") as file: #open the file made from the template
        tempdata = file.read() #read the file
        tempdata = tempdata.replace(textToSearchInstanceType, textToReplaceInstanceType) #replacing the term with a user provided answer

    with open("CFtemp.json", "w") as file: #open the file again to write the changes to the file
        file.write(tempdata) #writing the replaced terms to the file
        file.close() #closing the file


def ImageIDChange():
    with open("CFtemp.json", "r") as file:
        tempdata = file.read()
        tempdata = tempdata.replace(textToSearchImageID, textToReplaceImageID)

    with open("CFtemp.json", "w") as file:
        file.write(tempdata)
        file.close()

def instanceNameChange():
    with open("CFtemp.json", "r") as file:
        tempdata = file.read()
        tempdata = tempdata.replace(textToSearchInstanceName, textToReplaceInstanceName)

    with open("CFtemp.json", "w") as file:
        file.write(tempdata)
        file.close()


#Queries users for inputs to be inserted into template.
InstanceType = input("Insert instance type:")
if InstanceType == "": #if the user inputs nothing, an error pops up.
    print("No instance type inserted")
else: #if the user inputs anything else, that input is then declared as the string that will be put in place of the term in the .json file.
    textToReplaceInstanceType = InstanceType
    instanceTypeChange() #the coresponding function to replace the term with the user input variable is then called.

ImageID = input("Insert ImageID:")
if ImageID == "":
    print("No instance type inserted")
else:
    textToReplaceImageID = ImageID
    ImageIDChange()

InstanceName = input("Insert instance name:")
if InstanceName == "":
    print("No instance type inserted")
else:
    textToReplaceInstanceName = InstanceName
    instanceNameChange()

