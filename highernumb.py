# def pig_it(text):
#     specchars = [",", "!", "?", ".", "&", "#"]
#     wordlist = []
#     newtext = text.split()
#     for x in newtext:
#         if x in specchars:
#             wordlist.append(x)
#         else:
#             firstletter = x[0]
#             x = x[1:]
#             x += firstletter + "ay"
#             wordlist.append(x)
#     print(" ".join(wordlist))
                        
# pig_it("O tempora o mores !")

a = [1, 2, 3, 4]
x = sum(a)
print(x)