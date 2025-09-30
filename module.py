class OptionList:

    def __init__(self, optionType, userInput, label):
        self.optionType = optionType
        self.userInput = userInput
        self.label = label

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
            

            
class AdvancedConstruction:
    def __init__(self):

        stateA = "<incomplete>"
        stateB = "<complete>"
        stateC = " <optional>"
        stateD = " <required>"

        formatStateOne = stateA
        formatStateTwo = stateD
        descriptionStateOne = stateA
        descriptionStateTwo = stateD
        metadataStateOne = stateA
        metadataStateTwo = stateC
        parametersStateOne = stateA
        parametersStateTwo = stateC
        rulesStateOne = stateA
        rulesStateTwo = stateC
        mappingsStateOne = stateA
        mappingsStateTwo = stateC
        conditionsStateOne = stateA
        conditionsStateTwo = stateC
        transformsStateOne = stateA
        transfornsStateTwo = stateC
        resourcesStateOne = stateA
        resoucresStateTwo = stateD
        outputsStateOne = stateA
        outputsStateTwo = stateC

        message = f"""

        Here are the 10 different options to configure to complete your template.
        \n 1: Format Version {formatStateOne}{formatStateTwo} 
        \n 2: Description {descriptionStateOne}{descriptionStateTwo} 
        \n 3: Metadata {metadataStateOne} {metadataStateTwo}
        \n 4: Parameters {parametersStateOne} {parametersStateTwo}
        \n 5: Rules {rulesStateOne} {rulesStateTwo}
        \n 6: Mappings {mappingsStateOne} {mappingsStateTwo}
        \n 7: Conditions {conditionsStateOne} {conditionsStateTwo}
        \n 8: Transform {transformsStateOne} {transfornsStateTwo}
        \n 9: Resources {resourcesStateOne} {resoucresStateTwo}
        \n 10: Outputs {outputsStateOne} {outputsStateTwo}
        
        """
        print(message)

