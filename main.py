from docx import Document
import os

def Title():
    print("============================================")
    print("     Automated Find and Replace Script      ")
    print("============================================")
    print("Created By: Ashton Sidhu")
    print("Script that creates multiple files by replacing select words in a file template.")
    print("")

def ReadRepFile(repFile):
   
    with open(os.path.expanduser('~/Documents/' + repFile + ".txt")) as rFile:
        lines = rFile.readlines()    
    lines = [x.strip().replace(" ", "").replace("=", ":").split(",") for x in lines]
    return lines

def ReadTempFile(tempFile):
    doc = Document((os.path.expanduser('~/Documents/' + tempFile + ".docx")))

    docText = ""
    
    for para in doc.paragraphs:
        docText += para.text

    return docText

def ListToDic(li):      
    
    replaceDict = [dict([x.split(':') for x in item]) for item in li]

    return replaceDict     

def TextReplace(doc, repDict):

    for key in repDict:
        doc.replace(key, repDict[key])

    return doc

def main():
    Title()
    
    #Collect initial parameters: template file name, word replace file
    print("Ensure your template file and replace file are in your Documents folder.")
    tempFileName = input("Enter template file: ")    
    repFileName = input("Enter number of words to replace file: ")

    #Read and parse words to replace and how many files to create.
    repContent = ReadRepFile(repFileName)
    fileContent = ReadTempFile(tempFileName)

    #Convert list of words to replace to a dictionary
    repContent = ListToDic(repContent)
   
    #Replace words in the document with the words specified from the user
    for dic in repContent:
        TextReplace(fileContent, dic)

if __name__ == '__main__':
    main()
    