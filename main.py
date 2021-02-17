import os


def __read_file__(fileName):
    file = open(fileName)
    print(file.read())

def __write_file__(fileName, text):
    file = open(fileName, "w")
    file.write(text)

def __delete_file__(fileName):
    os.remove(fileName)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Would you like to read, write or delete a file?")
    print("1 - read")
    print("2 - write")
    print("3 - delete")
    choice = input("enter number:")
    if choice == "1":
        print("Please enter the file name you would like to read")
        choice2 = input("file name: ")
        __read_file__(choice2)
    elif choice == "2":
        print("Please enter the name of the file you want to write")
        choice3 = input("file name: ")
        print("Please enter the text you want to write in the file")
        text = input("file content: ")
        __write_file__(choice3, text)
    elif choice == "3":
        print("Give the name of the file you want to delete")
        deleteFile = input("file name: ")
        __delete_file__(deleteFile)
        print("File deleted")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
