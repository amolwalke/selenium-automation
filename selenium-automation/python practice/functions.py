class player:
    def move_right():
        print("move to right")
    def move_Left():
        print("move to Left")
    def move_top():
        print("move to top")
    def move_down():
        print("move to down")


name= input("press a arrow: ")
str(name)
www={'a','s','w','d'}
for i in www:
    if i == name:
        print(move_Left)
    elif i == name: 
        print(move_down)
    elif  i == name:
        print(move_top)
    elif i == name:
        print(move_right)

player1 = player()
player.move_Left()
player.move_right()
player.move_down()
player.move_top()