import docx
import os

def Title():
    print("============================================")
    print("     Automated Find and Replace Script      ")
    print("============================================")
    print("Created By: Ashton Sidhu")
    print("Script that creates multiple files by replacing select words in a file template.")
    print("")

def readRepFile(repFile):
   
    with open(os.path.expanduser('~/Documents/' + repFile)) as rFile:
        lines = rFile.readlines()    
    lines = [x.strip().replace(" ", "").split(",") for x in lines]
    return lines
    
def main():
    Title()
    
    #Collect initial parameters: template file name, word replace file
    print("Ensure your template file and replace file are in your Documents folder.")
    tempFileName = input("Enter template file: ")    
    repFileName = input("Enter number of words to replace file: ")

    #Read and parse words to replace and how many files to create.
    repContent = readRepFile(repFileName)
    print(repContent)     

if __name__ == '__main__':
    main()
    