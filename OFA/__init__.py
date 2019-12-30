from tkinter import *
import random
import time

def create_canvas(LS=160):
	tk=Tk()
	canvas = Canvas(tk, width=(LS+1)*5, height=760)
	canvas.pack()
	return tk, canvas

tk, canvas = create_canvas()
blocks = []

class Block:
	def __init__(self, canvas, x1, y1, x2, y2, colour):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.h = y2-y1
		self.img=canvas.create_rectangle(x1, y1, x2, y2, fill=colour)

def swap(b1, b2, list=blocks, tk=tk, canvas=canvas):
	dist = list[b2].x1-list[b1].x1
	canvas.move(list[b1].img, dist, 0)
	canvas.move(list[b2].img, -dist, 0)
	tk.update()
	list[b1].x1 += dist
	list[b2].x1 -= dist
	list[b1].x2 += dist
	list[b2].x2 -= dist
	list[b1], list[b2] = list[b2], list[b1]

def shuffle(LS=140, list=blocks, tk=tk, canvas=canvas):
	for i in range(0, LS):
		c=random.randrange(0, LS, 1)
		swap(i, c, list)

def generate(LS=140, list=blocks, canvas=canvas):
	for i in range(0, LS):
		list.append(Block(canvas, 3+5*i, 0, 8+5*i, 10+5*i, "red"))

def insert(index, ele, list=blocks, tk=tk, canvas=canvas):
	canvas.delete(list[index].img)
	canvas.delete(ele.img)
	list[index] = Block(canvas, list[index].x1, ele.y1, list[index].x2, ele.h+ele.y1, "red")
	tk.update()
