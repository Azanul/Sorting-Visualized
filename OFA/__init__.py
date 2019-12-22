from tkinter import *
import random
import time

def create_canvas(LS):
	tk=Tk()
	canvas = Canvas(tk, width=(LS+1)*5, height=760)
	tk.title("Sorting visualized")
	canvas.pack()
	return tk, canvas

class Block:
	def __init__(self, canvas, x1, y1, x2, y2, colour):
		self.x1=x1
		self.x2=x2
		self.h=y2-y1
		self.img=canvas.create_rectangle(x1, y1, x2, y2, fill=colour)

def swap(tk, canvas, list, b1, b2):
	temp=list[b2].x1-list[b1].x1
	canvas.move(list[b1].img, temp, 0)
	canvas.move(list[b2].img, -temp, 0)
	tk.update()
	list[b1].x1+=temp
	list[b2].x1-=temp
	list[b1].x2+=temp
	list[b2].x2-=temp
	list[b1], list[b2] = list[b2], list[b1]

def shuffle(tk, canvas, list, LS):
	for i in range(0, LS):
		c=random.randrange(0, LS, 1)
		swap(tk, canvas, list, i, c)

def generate(canvas, list, LS):
	for i in range(0, LS):
		list.append(Block(canvas, 3+5*i, 0, 8+5*i, 10+5*i, "red"))