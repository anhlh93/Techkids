px=2
py=1
bx=3
by=3

screen_height=7
screen_width=7
def showmap(px,py,bx,by):
    for y in range(screen_height):
        for x in range(screen_width):
            if x==px and y==py:
                print("P ",end="")
            elif x==bx and y==by:
                print("B ",end="")
            else:
                print("- ",end="")
        print()
def check_choice():
    if choice=="W" or choice=="S" or choice=="A" or choice=="D":
        return True
    return False
def move(choice,px,py):
    if choice=="W":
        return(px,py-1)
    if choice=="S":
        return(px,py+1)
    if choice=="A":
        return(px-1,py)
    if choice=="D":
        return(px+1,py)
def check_move(x,y):
    if x<0 or y<0 or x>screen_width-1 or y>screen_height-1:
        return False
    return True
while True:
    showmap(px,py,bx,by)
    choice=input("What do you want? UP(W) - DOWN(S) - LEFT (A) - RIGHT (D)").upper()
    if not check_choice:
        print("Wrong input!!!")
        continue
    (next_px,next_py)=move(choice,px,py)
    if check_move(next_px,next_py):
        if next_px==bx and next_py==by:
            (next_bx,next_by)=move(choice,bx,by)
            if check_move(next_bx,next_by):
                (bx,by)=(next_bx,next_by)
                (px,py)=(next_px,next_py)
            else:
                print("Cannot move")
        else:
            (px, py) = (next_px, next_py)
    else:
        print("Cannot move")




