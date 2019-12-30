from OFA import *


def sort(list=blocks):

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

				insert(k, l[i], list)

				i+=1

			else:

				insert(k, r[j], list)

				j+=1

			k+=1

			time.sleep(0.05)

		while i<mid:

			insert(k, l[i], list)

			time.sleep(0.05)

			i+=1

			k+=1

		while j<len(r):

			insert(k, r[j], list)

			time.sleep(0.05)
			j+=1

			k+=1


if __name__ == "__main__":

	tk.title("Merge Sort")


	generate()

	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle())

	btn2 = Button(tk, text = 'Sort', bd = '5', command = lambda: sort())

	btn1.pack(side='left')

	btn2.pack(side='left')

	tk.mainloop()