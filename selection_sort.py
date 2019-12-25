from OFA import *

SIZE=140
tk, canvas=create_canvas(SIZE)
def sort():
	for i in range(0, SIZE):
		min=i
		for j in range(i+1, SIZE):
			if blocks[min].h > blocks[j].h:
				min=j
		swap(tk, canvas, blocks, i, min)
		time.sleep(0.05)	
blocks=[]
generate(canvas, blocks, SIZE)
btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
btn2 = Button(tk, text = 'Sort', bd = '5', command = sort)
btn1.pack(side='left')
btn2.pack(side='left')
tk.mainloop()