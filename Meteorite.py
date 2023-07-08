import time


class Meteorite:
    def __init__(self,canvas, x, y, diameter, image,color, xVelocity, yVerlocity,locate):
        self.meteorite=canvas.create_rectangle(x, y, x+diameter, y+diameter, fill=color)
        #self.meteorite=canvas.create_image(x, y, image=image, anchor=locate)
        self.xVelocity=xVelocity
        self.yVelocity=yVerlocity
        self.canvas=canvas
        self.coordinate=[]
        self.diameter=diameter

    def move(self):
        self.canvas.move(self.meteorite, self.xVelocity, self.yVelocity)
        self.coordinate=self.canvas.coords(self.meteorite)
        
             
    def __del__(self):
        print("đã huỷ")
