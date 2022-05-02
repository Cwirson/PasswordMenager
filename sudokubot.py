from tkinter import *
from random import *

fillednumbersstart = int(input("how many numbers do you want to be filled at the beginning? (10 -- 80): "))

map9x9 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

window = Tk()

mapscreen = Label(window)
mapscreen.pack()

def solved():
    if "" or 0 not in map9x9[0] and "" or 0 not in map9x9[1] and "" or 0 not in map9x9[2] and "" or 0 not in map9x9[3] and "" or 0 not in map9x9[4] and "" or 0 not in map9x9[5] and "" or 0 not in map9x9[6] and "" or 0 not in map9x9[7] and "" or 0 not in map9x9[8]:
        return True
    else:
        return False
    
def randomplacenumber():
    if map9x9[row][column]["text"] == "0":
        global randrow, randcol, randnumb
        randrow = randrange(0, 9)
        randcol = randrange(0, 9)
        randnumb = randrange(1, 10) 
        return [randrow, randcol, randnumb]
    else:
        randomplacenumber()

for row in range(9):
    for column in range(9):
        map9x9[row][column] = Button(mapscreen, text="0", font=("consolas", 20), width=3, height=1)
        map9x9[row][column].grid(row = row, column = column)

for _ in range(fillednumbersstart):
    randomplacenumber()
    map9x9[randrow][randcol]["text"] = randnumb
    
window.mainloop()