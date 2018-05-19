

def Title():
    print("============================================")
    print("     Automated Find and Replace Script      ")
    print("============================================")
    print("")
    
def main():
    Title()
    
    #Collect initial parameters: template file name, number of files to output, num of words to replace
    fileName = input("Enter template file: ")
    numOfFiles = int(input("Enter number of files to output: "))
    numOfWords = int(input("Enter number of words to replace: "))

    print(fileName)
    print(numOfFiles)

if __name__ == '__main__':
    main()
    