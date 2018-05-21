from docx import Document
import os
import re

def Title():
    print("==================================================================================")
    print("Automated Find and Replace Script")
    print()
    print("Created By: Ashton Sidhu")
    print("Script that creates multiple files by replacing select words in a file template.")
    print("==================================================================================")
    print()

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
        
        doc = re.sub( "\\b" + key + "\\b" ,  repDict[key], doc )

    return doc

def WriteToFile(fileContent, index):
    doc = Document()

    doc.add_paragraph(fileContent)

    doc.save(os.path.expanduser('~/Documents/file' + str(index) + '.docx'))

def main():
    Title()
    
    #Collect initial parameters: template file name, word replace file
    print("Ensure your template file and replace file are in your Documents folder.")
    tempFileName = input("Enter template file: ")    
    repFileName = input("Enter number of words to replace file: ")

    #Read and parse words to replace and how many files to create.
    repContent = ReadRepFile(repFileName)
    docContent = ReadTempFile(tempFileName)

    #Convert list of words to replace to a dictionary
    repContent = ListToDic(repContent)
   
    #Replace words in the document with the words specified from the user
    print()
    for idx, dic in enumerate(repContent):
        fileContent = TextReplace(docContent, dic)
        WriteToFile(fileContent, idx)
        print("File " + str(idx) + " has been created.")

    print("")
    print("All files have been created successfully.")


if __name__ == '__main__':
    main()
    