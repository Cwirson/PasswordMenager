def checkpasswords():
    file = open("passwords.txt")
    linestoprint = input("which lines do you need to print? (a -> b): ").split()
    
    for index, line in enumerate(file, 1):
        if str(index) in linestoprint:
            print(f"{index} password is: {line}", end="")