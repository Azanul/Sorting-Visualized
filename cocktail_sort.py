from OFA import *

def sort(list=blocks): 
	LS = len(list)
	for i in range(LS):  
		for j in range(0, LS-i-1): 
			if list[j].h > list[j+1].h : 
				swap(j, j+1, list)
		for j in range(LS-i-2, i, -1): 
			if list[j].h > list[j+1].h : 
				swap(j, j+1, list)

if __name__ == "__main__":
	tk, canvas=create_canvas()
	tk.title("Cocktail Sort")
	generate()
	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle())
	btn2 = Button(tk, text = 'Sort', bd = '5', command = sort())
	btn1.pack(side='left')
	btn2.pack(side='left')
	tk.mainloop() 