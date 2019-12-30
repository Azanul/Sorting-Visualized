from OFA import *


def sort(high, low=0, list=blocks):

	if low < high:
 
		pi = partition(list, low, high)
 
		sort(pi-1, low, list)
 
		sort(high, pi+1, list)



def partition(list, low, high):
 
	i = low-1
 
	pivot = list[high].h


	for j in range(low, high):

		if list[j].h < pivot:
 
			i = i+1
 
			swap(i, j, list)

			time.sleep(0.04)

	swap(i+1, high, list)

	return (i+1)


if __name__ == "__main__":

	tk.title("Quick Sort")
	generate()

	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle())

	btn2 = Button(tk, text = 'Sort', bd = '5', command = lambda: sort(tk, canvas, blocks, SIZE))

	btn1.pack(side='left')

	btn2.pack(side='left')

	tk.mainloop()