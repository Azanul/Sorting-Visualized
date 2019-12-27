from OFA import *

SIZE=140
tk, canvas=create_canvas(SIZE)
tk.title("Heap Sort")
def heapify(list, n, i): 
	largest = i 
	l = 2*i+1
	r = 2*i+2
	if l < n and list[i].h < list[l].h: 
        	largest = l 

	if r < n and list[largest].h < list[r].h: 
		largest = r

	if largest != i:
		swap(tk, canvas, list, i, largest)
		time.sleep(0.03)
		heapify(list, n, largest)

def sort(): 
	n = len(blocks)
	for i in range(n, -1, -1): 
		heapify(blocks, n, i) 

	for i in range(n-1, 0, -1): 
		swap(tk, canvas, blocks, i, 0)
		time.sleep(0.03)
		heapify(blocks, i, 0)

blocks=[]
generate(canvas, blocks, SIZE)
btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
btn2 = Button(tk, text = 'Sort', bd = '5', command = sort)
btn1.pack(side='left')
btn2.pack(side='left')
tk.mainloop()