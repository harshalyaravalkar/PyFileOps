def creatf(name): # This function creates a empty text file
    file = open(f"{name}.txt","a")
    file.close()


def readf(name): # This function reads and returns content of text file
    file = open(f"{name}.txt","r")
    content = file.read()
    file.close()
    return content

def writef(text,filename): # This function rewrites file with user input text
    file = open(f"{filename}.txt","w")
    charlen = file.write(text)
    print(f"You have successfully written in file, Total Character Length: {charlen}")
    file.close()

def addf(text, filename): # This function adds the text without rewriting the file 
    file = open(f"{filename}.txt","a")
    charlen = file.write(f"\n{text}")
    print(f"You have successfully written in file, Total Character length: {charlen}")
    file.close()

def database(data): # This function adds records in database file
    file = open("database.txt","a")
    for i,n,a,l in data:
        file.write(f"{i:5} {n:15} {a:3} {l:12}\n")
        print(f"{i:5} {n:15} {a:3} {l:12}")
    file.close()


while True:
    print("File Handling".center(50,"="))
    print("To Work with: \n 1. Create a Text File \n 2. Text File \n 3. Structured data file \n 4. Exit\n")
    s = input("Enter your selection: ")

    if(s=="1"): #Create text file
         name = input("Enter name of file: ")
         creatf(name)
         continue

    if(s=="2"): # Actions on text file
        print("\nText File: \n 1. Read text File \n 2. Overwrite text file \n 3. Add text into file \n 4. Main menu \n")
        n = input("Enter your selection: ")

        if(n=="1"): # Reading text file
            name = input("Enter name of file: ")
            content = readf(name)
            print(f"\n\n{content}\n")
            continue

        if(n=="2"): # Rewriting content in file
            text = input("Enter the text content you want to add: ")
            filename = input("Enter the filename: ")
            writef(text,filename)
            continue

        if(n=="3"): # Adding content in file
            text = input("Enter the text you want to add in existing content of file: ")
            filename = input("Enter the file name: ")
            addf(text,filename)
            continue
        else:
            continue

    if(s=="3"): # Actions on database file
        print("\nStructured Data: \n 1. Read Structured Data File \n 2. Add Records \n 3. Exit\n")
        r = input("Enter your selection: ")

        if(r=="1"): # Read database file
            name = input("Enter name of file: ")
            content = readf(name)
            print(f"\n\n{content}\n")
            continue

        if(r=="2"): # Add records in database file
            print("Enter data in the file: ")
            ids = input("Enter the id: ")
            name = input("Enter the name: ")
            age= input("Enter the age: ")
            add = input("Enter the address : ")

            data = [[ids,name,age,add]]
            database(data)
            continue
        
        else:
            continue # Takes back to main menu

    else:
        break # Ends program
