from passwordmenager import checkpasswords

f = open("passwords.txt", "w")
f.close()

def inputpassword():
    password = input("input password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{password}\n")

hmpasswords = int(input("how many passwords input: "))
for x in range(hmpasswords):
    inputpassword()
    
x = input("done? Y/N: ").upper()
if x == "Y":
    pass
elif x == "N":
    checkpasswords()
else:
    print("invalid option")