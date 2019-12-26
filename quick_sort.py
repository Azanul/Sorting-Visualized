from OFA import *

SIZE=140
tk, canvas=create_canvas(SIZE)
tk.title("Quick Sort")
def sort(list, low, high):
	if low < high: 
		pi = partition(list, low, high) 
		sort(list, low, pi-1) 
		sort(list, pi+1, high)

def partition(list, low, high): 
	i = low-1 
	pivot = list[high].h

	for j in range(low, high):
		if list[j].h < pivot: 
			i = i+1 
			swap(tk, canvas, list, i, j)
			time.sleep(0.04)
	swap(tk, canvas, list, i+1, high)
	return (i+1)

blocks=[]
generate(canvas, blocks, SIZE)
btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
btn2 = Button(tk, text = 'Sort', bd = '5', command = lambda: sort(blocks, 0, SIZE-1))
btn1.pack(side='left')
btn2.pack(side='left')
tk.mainloop()