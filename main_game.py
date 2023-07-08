from tkinter import *
from Meteorite import *
import time
import random

WIDTH=700
HEIGHT=600
DIAMETER_SPACESHIP=100
COLOR_METEORITE=["yellow", "pink", "blue", "red", "green"]

class Spaceship():
    def __init__(self):
        x=WIDTH/2-DIAMETER_SPACESHIP/2
        y=HEIGHT-DIAMETER_SPACESHIP
        #self.spaceship=canvas.create_oval(x, y, x+DIAMETER_SPACESHIP, y+DIAMETER_SPACESHIP, fill="black")
        self.spaceship=canvas.create_image(x,y,image=ufo_image, anchor=NW)
        self.diameter_spaceship=DIAMETER_SPACESHIP
        self.coordinate=canvas.coords(self.spaceship)
#create meteorite
def new_meteorite():
    diameter=random.randint(30,200)
    color=random.choice(COLOR_METEORITE)
    image=random.choice(my_meteorite)
    image1=random.choice(my_image)
    image2=create_image(image,diameter)
    x=random.randint(0,700)
    xVelocity=random.randint(-3,3)
    yVelocity = random.randint(4, 10)
    return Meteorite(canvas, x,-diameter, diameter, image1,color, xVelocity, yVelocity,NW)
#create multi meteorite
def rain_meteorite():
    global continue_play
    second=random.randint(800,3000)
    Turn_on(new_meteorite())
    if continue_play:
        window.after(second,rain_meteorite )
        window.update()

#control spaceship
def spaceship_move(event,spaceship):
    global continue_play
    x=spaceship.coordinate[0]
    y=spaceship.coordinate[1]
    if continue_play:                #check overgame
        if event=="up":
            if y<=0:
                pass
            else:
                canvas.move(spaceship.spaceship, 0, -30)
        elif event=="down":
            if y>=HEIGHT-DIAMETER_SPACESHIP:
                pass
            else:
                canvas.move(spaceship.spaceship, 0, 30)
        elif event == "left":
            if x<=0:
                pass
            else:
                canvas.move(spaceship.spaceship, -30, 0)
        elif event == "right":
            if x>=WIDTH-DIAMETER_SPACESHIP:
                pass
            else:
                canvas.move(spaceship.spaceship, 30, 0)
    spaceship.coordinate=canvas.coords(spaceship.spaceship)

def check_collision(coordinate,diameter):
    global spaceship
    x=spaceship.coordinate[0]
    y=spaceship.coordinate[1]
    diameter_spaceship=spaceship.diameter_spaceship
    if coordinate[0]-diameter_spaceship <x<coordinate[0]+diameter and coordinate[1]-diameter_spaceship <y<coordinate[1]+diameter:
        return True
    else:
        return False

def Turn_on(meteorite):
    global spaceship
    global continue_play
    global start
    meteorite.move()
    current=time.perf_counter()
    label_score.config(text=f"Score:{int(current-start)}")
    window.update()
    coordinate=meteorite.coordinate
    if check_collision(coordinate, meteorite.diameter): #check collision
        continue_play=False
        gameover()
        return
    if coordinate[0] > WIDTH or coordinate[0] < -meteorite.diameter or coordinate[1] > HEIGHT: # if meteorite have been out screen, delete it
        del meteorite
        return
    if continue_play:
        window.after(50, Turn_on, meteorite)
def gameover():
    global spaceship
    x=window.winfo_width()
    y=window.winfo_height()
    lose=Label(window, text="Game over", font=("consolas", 50),fg="red")
    lose.place(x=x/2, y=y/2, anchor=CENTER)
def create_image(image, diameter):
    x=image.width()
    y=image.height()
    x=int(x/diameter)
    y=int(y/diameter)
    my_image=image.subsample(x,y)
    return my_image



window=Tk()
window.title("Meteorite")

label_score=Label(window, text="Score:0", font=("consolas", 25), fg="blue")
label_score.pack()

ufo=PhotoImage(file="picture/ufo.png")
meteorite_image1=PhotoImage(file="picture/meteorite1.png")
meteorite_image2=PhotoImage(file="picture/meteorite2.png")
meteorite_image3=PhotoImage(file="picture/meteorite3.png")
meteorite_image4=PhotoImage(file="picture/meteorite4.png")
my_meteorite=[meteorite_image4,meteorite_image1,meteorite_image3,meteorite_image2]
my_image=[]

background=PhotoImage(file="picture/background.png")
background=create_image(background,WIDTH)
width_ufo=ufo.width()
height_ufo=ufo.height()
width_ufo=int(width_ufo/DIAMETER_SPACESHIP)
height_ufo=int(height_ufo/DIAMETER_SPACESHIP)
ufo_image=ufo.subsample(width_ufo,height_ufo)

canvas=Canvas(window)
canvas.config(height=HEIGHT, width=WIDTH)
canvas.pack()
canvas.create_image(0, 0, image=background, anchor=NW)
for image in my_meteorite:
    my_image.append(create_image(image,100))

continue_play=True
spaceship=Spaceship()
start=time.perf_counter()
rain=rain_meteorite()


window.bind("<w>", lambda event: spaceship_move("up", spaceship))
window.bind("<s>", lambda event: spaceship_move("down",spaceship))
window.bind("<a>", lambda event: spaceship_move("left",spaceship))
window.bind("<d>", lambda event: spaceship_move("right",spaceship))
window.bind("<Up>", lambda event: spaceship_move("up", spaceship))
window.bind("<Down>", lambda event: spaceship_move("down",spaceship))
window.bind("<Left>", lambda event: spaceship_move("left",spaceship))
window.bind("<Right>", lambda event: spaceship_move("right",spaceship))

window.update()

width_game=window.winfo_width()
height_game=window.winfo_height()
width_screen=window.winfo_screenwidth()
height_sreen=window.winfo_screenheight()
x=int(width_screen/2-width_game/2)
y=int(height_sreen/2-height_game/2)
window.geometry(f"{width_game}x{height_game}+{x}+{y}")

window.mainloop()