from OFA import *

if __name__ == "__main__":
	tk.title("Radix Sort")
	generate(SIZE)
	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle())
	btn2 = Button(tk, text = 'Sort', bd = '5', command = lambda: sort())
	btn1.pack(side='left')
	btn2.pack(side='left')
	tk.mainloop()

def countingSort(arr, exp1):
	n = len(arr)
	output = [0]*(n)
	count = [0]*(10)
	for i in range(0, n):
		index = int(arr[i].h/exp1)
		count[(index)%10] += 1
	for i in range(1,10):
        	count[i] += count[i-1]
	i = n-1

	while i>=0:
		index = int(arr[i].h/exp1)
		output[ count[ (index)%10 ] - 1] = arr[i]
		count[ (index)%10 ] -= 1
		i -= 1
	i = 0
	for i in range(0,len(arr)):
		insert(i, output[i], arr)

def sort(list=blocks):
	max1 = max(list, key=lambda block: block.h)
	exp = 1
	while max1.h//exp > 0:
		countingSort(list, exp)
		exp *= 10
