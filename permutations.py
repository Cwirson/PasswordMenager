import itertools

def permutations(string):
    newlist = []
    x = list(string)
    permutations = list(set((itertools.permutations(x))))
    for x in permutations:
        word = "".join(x)
        newlist.append(word)
    print(newlist)
        
permutations("aabb")