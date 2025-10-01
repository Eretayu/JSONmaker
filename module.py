class OptionList:

    def __init__(self, optionType, userInput, label, advanced_construction=None, option_number=None):
        self.optionType = optionType
        self.userInput = userInput
        self.label = label
        self.advanced_construction = advanced_construction
        self.option_number = option_number

    def addOptionType(self):
        with open("CFtemp.json", "r") as file: #open the file made from the template
            tempdata = file.read() #read the file
            tempdata = tempdata.replace(self.optionType, self.userInput) #replacing the term with a user provided answer

        with open("CFtemp.json", "w") as file: #open the file again to write the changes to the file
            file.write(tempdata) #writing the replaced terms to the file
            file.close() #closing the file

    def queryUser(self):
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

        stateA = "<incomplete>"
        stateB = "<complete>"
        stateC = " <optional>"
        stateD = " <required>"

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
        \n 1: Format Version {self.formatStateOne}{self.formatStateTwo} 
        \n 2: Description {self.descriptionStateOne}{self.descriptionStateTwo} 
        \n 3: Metadata {self.metadataStateOne} {self.metadataStateTwo}
        \n 4: Parameters {self.parametersStateOne} {self.parametersStateTwo}
        \n 5: Rules {self.rulesStateOne} {self.rulesStateTwo}
        \n 6: Mappings {self.mappingsStateOne} {self.mappingsStateTwo}
        \n 7: Conditions {self.conditionsStateOne} {self.conditionsStateTwo}
        \n 8: Transform {self.transformsStateOne} {self.transfornsStateTwo}
        \n 9: Resources {self.resourcesStateOne} {self.resoucresStateTwo}
        \n 10: Outputs {self.outputsStateOne} {self.outputsStateTwo}
        
        """
        print(self.message)
    
    def update_state(self, option_number):
        """Update the state of a specific option to complete"""
        stateB = "<complete>"
        
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
        \n 1: Format Version {self.formatStateOne}{self.formatStateTwo} 
        \n 2: Description {self.descriptionStateOne}{self.descriptionStateTwo} 
        \n 3: Metadata {self.metadataStateOne} {self.metadataStateTwo}
        \n 4: Parameters {self.parametersStateOne} {self.parametersStateTwo}
        \n 5: Rules {self.rulesStateOne} {self.rulesStateTwo}
        \n 6: Mappings {self.mappingsStateOne} {self.mappingsStateTwo}
        \n 7: Conditions {self.conditionsStateOne} {self.conditionsStateTwo}
        \n 8: Transform {self.transformsStateOne} {self.transfornsStateTwo}
        \n 9: Resources {self.resourcesStateOne} {self.resoucresStateTwo}
        \n 10: Outputs {self.outputsStateOne} {self.outputsStateTwo}
        
        """
        print(self.message)