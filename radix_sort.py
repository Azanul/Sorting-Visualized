from OFA import *

SIZE=140
tk, canvas=create_canvas(SIZE)
tk.title("Radix Sort")

def countingSort(arr, exp1): 
	n = len(arr) 
	output = [0]*(n) 
	count = [0]*(10)

	for i in range(0, n): 
		index = int(arr[i].h/exp1) 
		print(index)
		count[(index)%10] += 1
	print(count)
	for i in range(1,10): 
        	count[i] += count[i-1] 
	print(count)
	i = n-1
	while i>=0: 
		index = int(arr[i].h/exp1) 
		output[ count[ (index)%10 ] - 1] = arr[i] 
		count[ (index)%10 ] -= 1
		i -= 1

	i = 0
	for i in range(0,len(arr)): 
		insert(tk, canvas, arr, i, output[i]) 
  
def sort(): 
	max1 = max(blocks, key=lambda block: block.h)
	exp = 1
	while max1.h//exp > 0: 
		countingSort(blocks, exp) 
		exp *= 10

blocks=[]
generate(canvas, blocks, SIZE)
btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
btn2 = Button(tk, text = 'Sort', bd = '5', command = sort)
btn1.pack(side='left')
btn2.pack(side='left')
tk.mainloop()