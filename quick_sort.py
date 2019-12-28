from OFA import *

def sort(tk, canvas, list, high, low=0):
	if low < high: 
		pi = partition(tk, canvas, list, low, high) 
		sort(tk, canvas, list, pi-1, low) 
		sort(tk, canvas, list, high, pi+1)

def partition(tk, canvas, list, low, high): 
	i = low-1 
	pivot = list[high].h

	for j in range(low, high):
		if list[j].h < pivot: 
			i = i+1 
			swap(tk, canvas, list, i, j)
			time.sleep(0.04)
	swap(tk, canvas, list, i+1, high)
	return (i+1)

if __name__ == "__main__":
	SIZE=140
	tk, canvas=create_canvas(SIZE)
	tk.title("Quick Sort")
	blocks=[]
	generate(canvas, blocks, SIZE)
	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
	btn2 = Button(tk, text = 'Sort', bd = '5', command = lambda: sort(tk, canvas, blocks, SIZE))
	btn1.pack(side='left')
	btn2.pack(side='left')
	tk.mainloop()