from OFA import *

def sort(list=blocks):
	for i in range(0, len(list)):
		min=i
		for j in range(i+1, len(list)):
			if list[min].h > list[j].h:
				min=j
		swap(i, min, list)
		time.sleep(0.05)

if __name__ == "__main__":
	tk.title("Selection Sort")
	generate()
	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle())
	btn2 = Button(tk, text = 'Sort', bd = '5', command = sort())
	btn1.pack(side='left')
	btn2.pack(side='left')
	tk.mainloop()