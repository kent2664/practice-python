mainMenu = ("1.Add","2.Search","3.Remove", "4. Show All","5. Quit")
contacts = dict()
selectedOption = 0
def printMenu(menuItems):
    for item in menuItems:
        print(item)
def askYesNo(question):
    answer = input(question + " (y/n): ")
    return answer.lower() in ('y', 'yes')
def addContact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")
def searchContact():
    print( "Search contact" .center(50,"*"))
    query = input("Enter contact name to search: ").strip()
    if not query:
        print("Search query cannot be empty.")
        return
    key = query.lower()
    if key in contacts:
        foundContact = contacts[key]
        print(f"Contact found: {query} - {foundContact}")
    else:
        print("Contact not found.")
def removeContact():
    print( "Remove contact" .center(50,"*"))
    name = input("Name to remove: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    key = name.lower()
    if key in contacts:
        del contacts[key]
        print(f"Contact {name} removed.")
    else:
        print("Contact not found.")
def showAll():
    print( "All contacts" .center(50,"*"))
    for contact in contacts.values():
        for key,val in contact.items():
            print(f"{key} : {val}")
        print("*" *10)
while(selectedOption != 5):
    printMenu(mainMenu)
    selectedOption = int(input("Select an option (1-5): "))
    if(selectedOption not in range(1,6)):
        print("Invalid option. Please try again.")
        continue
    if(selectedOption == 1):
        addContact()
    elif(selectedOption == 2):
        searchContact()
    elif(selectedOption == 3):
        removeContact()
    elif(selectedOption == 4):
        showAll()
print("Bye bye :)")

import os
print("String format : ", os.getcwd())
print("Byte string format :", os.getcwdb())