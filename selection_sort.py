from OFA import *

def sort(tk, canvas, list):
	for i in range(0, len(list)):
		min=i
		for j in range(i+1, len(list)):
			if list[min].h > list[j].h:
				min=j
		swap(tk, canvas, list, i, min)
		time.sleep(0.05)

if __name__ == "__main__":
	SIZE=140
	tk, canvas=create_canvas(SIZE)
	tk.title("Selection Sort")
	blocks=[]
	generate(canvas, blocks, SIZE)
	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
	btn2 = Button(tk, text = 'Sort', bd = '5', command = sort(tk, canvas, blocks))
	btn1.pack(side='left')
	btn2.pack(side='left')
	tk.mainloop()