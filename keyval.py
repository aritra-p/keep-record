import json
d={}
helptext="\nInstructions:\n1. Create a new entry\n2. Read an existing entry\n3. Delete an existing entry\n4. Exit"
inp=-1
while (inp!=4):
    print(helptext)
    inp=int(input())
    if (inp==1):
        k=input("Enter the key: ")
        if (k not in d):
            v=input("Enter the value as JSON object: ")
            d[k]=json.loads(v)
            print("Key added successfully!")
        else:
            print("Key already exists!")
    elif (inp==2):
        k=input("Enter the key to be read: ")
        if (k in d):
            print("Value of asked key:")
            print(d[k])
        else:
            print("No such key exists!")
    elif (inp==3):
        k=input("Enter key to be deleted: ")
        if (k in d):
            del d[k]
            print("Key deleted successfully!")
        else:
            print("No such key exists!")
print("Thanks for using the program!")
