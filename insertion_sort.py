from OFA import *

SIZE=140
tk, canvas=create_canvas(SIZE)
tk.title("Insertion Sort")
def sort():
	for i in range(1, SIZE):
		for j in range(i-1, -1, -1):
			if blocks[i].h > blocks[j].h:
				break
			swap(tk, canvas, blocks, i, j)
			time.sleep(0.03)
			i-=1

blocks=[]
generate(canvas, blocks, SIZE)
btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
btn2 = Button(tk, text = 'Sort', bd = '5', command = sort)
btn1.pack(side='left')
btn2.pack(side='left')
tk.mainloop()