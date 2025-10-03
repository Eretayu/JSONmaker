class OptionList:

    def __init__(self, optionType, userInput, label, advanced_construction=None, option_number=None):
        self.optionType = optionType
        self.userInput = userInput
        self.label = label
        self.advanced_construction = advanced_construction
        self.option_number = option_number

        global explaination
        if self.option_number == 1:
            explaination = "The AWS Template Format Version is a date that specifies the latest version of formating that the template will conform to. The AWS JSONmaker uses the 2010-09-09 format version, which is the latest format version. For more information, head to the official AWS documentation at https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/format-version-structure"
        elif self.option_number == 2:
            explaination = "The Description is, very simply, any description you would like to give the template in order to remind yourself or others what it is for later. "
        elif self.option_number == 3:
            explaination = "The AWS metadata section contains any metadata you want the template to hold. For more information about formating requirements, head to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure"
        elif self.option_number == 4:
            explaination = "Parameters are a way to set values for different resources, so that they can be updated under the 'parameters' subheadin where they are more easily found. Parameters can be complicated, and their formating is difficult. For more information, head to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure"
        elif self.option_number == 5:
            explaination = "Rules are an optional way to make certain templates only take affect on certain contitions. For more information and formating requirements, head to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/rules-section-structure"
        elif self.option_number == 6:
            explaination = "Like rules, mappings are used to change certain values conditionally. For more info, head to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure"
        elif self.option_number == 7:
            explaination = "x"
        elif self.option_number == 8:
            explaination = "lesgo2"
        elif self.option_number == 9:
            explaination = "lesgo2"
        elif self.option_number == 10:
            explaination = "lesgo2"


    def addOptionType(self):
        with open("CFtemp.json", "r") as file: #open the file made from the template
            tempdata = file.read() #read the file
            tempdata = tempdata.replace(self.optionType, self.userInput) #replacing the term with a user provided answer

        with open("CFtemp.json", "w") as file: #open the file again to write the changes to the file
            file.write(tempdata) #writing the replaced terms to the file
            file.close() #closing the file

    def queryUser(self):
        print(explaination)
        userInput = input(f"Insert {self.label} for your Cloud Formation template here:")
        if userInput == "":
            print(f"No {self.label} inserted")
        else:
            self.userInput = userInput
            print(f"{self.label} inserted")
            self.addOptionType()
            # Update the advanced construction state if provided
            if self.advanced_construction and self.option_number:
                self.advanced_construction.update_state(self.option_number)
            

            
class AdvancedConstruction:
    def __init__(self):
        global RED
        global GREEN
        global WHITE
        global YELLOW
        RED = "\033[31m"
        GREEN = "\033[32m"
        WHITE = "\033[37m"
        YELLOW = "\033[33m"

        stateA = f"{RED}<incomplete>"
        stateC = f"{WHITE}<optional>"
        stateD = f"{RED} <required>"

        self.formatStateOne = stateA
        self.formatStateTwo = stateD
        self.descriptionStateOne = stateA
        self.descriptionStateTwo = stateD
        self.metadataStateOne = stateA
        self.metadataStateTwo = stateC
        self.parametersStateOne = stateA
        self.parametersStateTwo = stateC
        self.rulesStateOne = stateA
        self.rulesStateTwo = stateC
        self.mappingsStateOne = stateA
        self.mappingsStateTwo = stateC
        self.conditionsStateOne = stateA
        self.conditionsStateTwo = stateC
        self.transformsStateOne = stateA
        self.transfornsStateTwo = stateC
        self.resourcesStateOne = stateA
        self.resoucresStateTwo = stateD
        self.outputsStateOne = stateA
        self.outputsStateTwo = stateC

        self.message = f"""

        Here are the 10 different options to configure to complete your template.
        \n 1: Format Version {self.formatStateOne}{self.formatStateTwo}{WHITE}
        \n 2: Description {self.descriptionStateOne}{self.descriptionStateTwo}{WHITE}
        \n 3: Metadata {self.metadataStateOne} {self.metadataStateTwo}{WHITE}
        \n 4: Parameters {self.parametersStateOne} {self.parametersStateTwo}{WHITE}
        \n 5: Rules {self.rulesStateOne} {self.rulesStateTwo}{WHITE}
        \n 6: Mappings {self.mappingsStateOne} {self.mappingsStateTwo}{WHITE}
        \n 7: Conditions {self.conditionsStateOne} {self.conditionsStateTwo}{WHITE}
        \n 8: Transform {self.transformsStateOne} {self.transfornsStateTwo}{WHITE}
        \n 9: Resources {self.resourcesStateOne} {self.resoucresStateTwo}{WHITE}
        \n 10: Outputs {self.outputsStateOne} {self.outputsStateTwo}{WHITE}
        
        """
        print(self.message)
    
    def update_state(self, option_number):
        """Update the state of a specific option to complete"""
        stateB = f"{GREEN}<complete>"
        
        if option_number == 1:
            self.formatStateOne = stateB
        elif option_number == 2:
            self.descriptionStateOne = stateB
        elif option_number == 3:
            self.metadataStateOne = stateB
        elif option_number == 4:
            self.parametersStateOne = stateB
        elif option_number == 5:
            self.rulesStateOne = stateB
        elif option_number == 6:
            self.mappingsStateOne = stateB
        elif option_number == 7:
            self.conditionsStateOne = stateB
        elif option_number == 8:
            self.transformsStateOne = stateB
        elif option_number == 9:
            self.resourcesStateOne = stateB
        elif option_number == 10:
            self.outputsStateOne = stateB

        # Regenerate message with current states
        self.message = f"""

        Here are the 10 different options to configure to complete your template.
        \n 1: Format Version {self.formatStateOne}{self.formatStateTwo}{WHITE} 
        \n 2: Description {self.descriptionStateOne}{self.descriptionStateTwo}{WHITE} 
        \n 3: Metadata {self.metadataStateOne} {self.metadataStateTwo}{WHITE}
        \n 4: Parameters {self.parametersStateOne} {self.parametersStateTwo}{WHITE}
        \n 5: Rules {self.rulesStateOne} {self.rulesStateTwo}{WHITE}
        \n 6: Mappings {self.mappingsStateOne} {self.mappingsStateTwo}{WHITE}
        \n 7: Conditions {self.conditionsStateOne} {self.conditionsStateTwo}{WHITE}
        \n 8: Transform {self.transformsStateOne} {self.transfornsStateTwo}{WHITE}
        \n 9: Resources {self.resourcesStateOne} {self.resoucresStateTwo}{WHITE}
        \n 10: Outputs {self.outputsStateOne} {self.outputsStateTwo}{WHITE}
        
        """
        print(self.message)

