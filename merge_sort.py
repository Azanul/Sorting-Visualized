from OFA import *

SIZE=140
tk, canvas=create_canvas(SIZE)
tk.title("Merge Sort")
def sort(list):
	LS = len(list)
	if LS>1 :
		mid = LS//2
		l, r = list[:mid], list[mid:]

		sort(r)
		sort(l)
		for i in range(LS):
			canvas.delete(list[i].img)
		i=j=k=0
		while i<mid and j<len(r):
			if l[i].h < r[j].h:
				insert(tk, canvas, list, k, l[i])
				i+=1
			else:
				insert(tk, canvas, list, k, r[j])
				j+=1
			k+=1
			time.sleep(0.05)
		while i<mid:
			insert(tk, canvas, list, k, l[i])
			time.sleep(0.05)
			i+=1
			k+=1
		while j<len(r):
			insert(tk, canvas, list, k, r[j])
			time.sleep(0.05)		
			j+=1
			k+=1

blocks=[]
generate(canvas, blocks, SIZE)
btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
btn2 = Button(tk, text = 'Sort', bd = '5', command = lambda: sort(blocks))
btn1.pack(side='left')
btn2.pack(side='left')
tk.mainloop()