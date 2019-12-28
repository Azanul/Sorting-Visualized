from OFA import *

def sort(tk, canvas, list):
	LS = len(list)
	for i in range(1, LS):
		for j in range(i-1, -1, -1):
			if list[i].h > list[j].h:
				break
			swap(tk, canvas, list, i, j)
			time.sleep(0.03)
			i-=1

if __name__ == "__main__":
	SIZE=140
	tk, canvas=create_canvas(SIZE)
	tk.title("Insertion Sort")
	blocks=[]
	generate(canvas, blocks, SIZE)
	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
	btn2 = Button(tk, text = 'Sort', bd = '5', command = sort(tk, canvas, blocks))
	btn1.pack(side='left')
	btn2.pack(side='left')
	tk.mainloop()