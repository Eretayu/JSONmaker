class MetaData:
    #Metadata can list things about the whole template or about an individual resource
    
    def __init__(self, metadata, userInput):
        self.metadata = metadata
        self.userInput = userInput

    def addMetadata(self):
        with open("CFtemp.json", "r") as file: #open the file made from the template
            tempdata = file.read() #read the file
            tempdata = tempdata.replace(self.metadata, self.userInput) #replacing the term with a user provided answer

        with open("CFtemp.json", "w") as file: #open the file again to write the changes to the file
            file.write(tempdata) #writing the replaced terms to the file
            file.close() #closing the file

    def queryUser(self):
        userInput = input("Insert metadata for your Cloud Formation template here:")
        if userInput == "":
            print("No metadata inserted")
        else:
            self.userInput = userInput
            self.addMetadata()