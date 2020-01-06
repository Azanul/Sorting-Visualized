from OFA import *



def heapify(list, n, i):
 
	largest = i
 
	l = 2*i+1

	r = 2*i+2

	if l < n and list[i].h < list[l].h:
 
        	largest = l
 

	if r < n and list[largest].h < list[r].h:
 
		largest = r


	if largest != i:

		swap(i, largest, list)

		time.sleep(0.03)

		heapify(list, n, largest)



def sort(list=blocks):
 
	n = len(list)

	for i in range(n, -1, -1):
 
		heapify(list, n, i)
 

	for i in range(n-1, 0, -1):
 
		swap(i, 0, list)

		time.sleep(0.03)

		heapify(list, i, 0)



if __name__ == "__main__":

	tk.title("Heap Sort")

	blocks=[]

	generate()

	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle())

	btn2 = Button(tk, text = 'Sort', bd = '5', command = lambda: sort())

	btn1.pack(side='left')

	btn2.pack(side='left')

	tk.mainloop()