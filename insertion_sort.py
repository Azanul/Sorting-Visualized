from OFA import *

def sort(list=blocks):
	LS = len(list)
	for i in range(1, LS):
		for j in range(i-1, -1, -1):
			if list[i].h > list[j].h:
				break
			swap(i, j, list)
			time.sleep(0.03)
			i-=1

if __name__ == "__main__":
	tk, canvas=create_canvas()
	tk.title("Insertion Sort")
	generate()
	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle())
	btn2 = Button(tk, text = 'Sort', bd = '5', command = sort())
	btn1.pack(side='left')
	btn2.pack(side='left')
	tk.mainloop()