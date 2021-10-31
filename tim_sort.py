from OFA import *

Optimum_Size = 32
#Impacts On Chunk Size
#Change Value For Tuning Program Efficiency
#Approx Best 32 - 64

def CalcMinRun(n):
	while n >= Optimum_Size:
		n = n>> 1
	return n+1

def insertion_sort(arr,start,end):

	for i in range(start+1,end+1):
		k = arr[i]

		j = i - 1
		while k.h < arr[j].h and j >= start:
			insert(j+1,arr[j],arr)
			j -= 1

		insert(j+1,k,arr)
	return arr[start:end+1]


def merge_sort(arr,left,mid,right):
	larr = arr[left:mid]
	lenl = mid - left

	rarr = arr[mid:right+1]
	lenr = right - mid

	p1 = p2 = 0
	k = left
	while p1<lenl and p2<lenr:
		if larr[p1].h < rarr[p2].h:
			insert(k, larr[p1], arr)
			p1 += 1
		elif rarr[p2].h < larr[p1].h:
			insert(k, rarr[p2], arr)
			p2 += 1
		else:
			insert(k, larr[p1], arr)
			k += 1
			insert(k, rarr[p2], arr)
			p1 += 1
			p2 += 1
		k += 1

	while p1<lenl:
		insert(k, larr[p1], arr)
		p1 += 1
		k += 1

	while p2<lenr:
		insert(k, rarr[p2], arr)
		p2 += 1
		k += 1


def sort(lst=blocks):
	size = len(lst)
	runs = CalcMinRun(size)

	#Insertion Sort
	start = 0
	end = 0
	while end < size-1:
		start = end
		end = runs + start
		if end >= size: end = size-1
		insertion_sort(lst,start,end)

	#Merge Sort
	chunk = runs
	while chunk <= size:
		chunk = 2 * chunk
		for start in range(0,size,chunk):
			left = start
			mid = min(left+(chunk//2),size-1)
			right = min(left+chunk,size-1)
			if mid <= right:
				merge_sort(lst,left,mid,right)


if __name__ == "__main__":
	tk.title("TimSort")
	generate()
	btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle())
	btn2 = Button(tk, text = 'Sort', bd = '5', command = lambda: sort())
	btn1.pack(side='left')
	btn2.pack(side='left')
	tk.mainloop() 