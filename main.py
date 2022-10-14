from heap_sort import sort as HS

from insertion_sort import sort as IS

from merge_sort import sort as MS

from quick_sort import sort as QS

from radix_sort import sort as RS

from selection_sort import sort as SS

from bubble_sort import sort as BS

from cocktail_sort import sort as CS

from bucket_sort import sort as BuS

from shell_sort import sort as SS

from tim_sort import sort as TiS

from OFA import *

tk.title("Sorting Visualized")

generate()

net_blocks_var = Variable(tk, value= 140)

net_blocks = lambda: int(net_blocks_var.get())

inputBox = Entry(tk, textvariable= net_blocks_var)

enter = Button(tk, text= 'Enter', bd= '5', command= lambda: reset(net_blocks()))

btn1 = Button(tk, text='Shuffle', bd='5', command=lambda: shuffle(net_blocks()))

btn2 = Button(tk, text='Insertion Sort', bd='5', command=lambda: IS())

btn3 = Button(tk, text='Selection Sort', bd='5', command=lambda: SS())

btn4 = Button(tk, text='Merge Sort', bd='5', command=lambda: MS())

btn5 = Button(tk, text='Quick Sort', bd='5', command=lambda: QS(net_blocks() - 1))

btn6 = Button(tk, text='Heap Sort', bd='5', command=lambda: HS())

btn7 = Button(tk, text='Radix Sort', bd='5', command=lambda: RS())

btn8 = Button(tk, text='Bubble Sort', bd='5', command=lambda: BS())

btn9 = Button(tk, text='Cocktail Sort', bd='5', command=lambda: CS())

btn10 = Button(tk, text = 'Shell Sort', bd = '5', command = lambda: SS())

btnAmbareen = Button(tk, text='Bucket Sort', bd='5', command=lambda: BuS())

btnAman = Button(tk, text='Tim Sort', bd='5', command=lambda: TiS())

btn1.place(x=710, y=5)

inputBox.place(x=710, y=45)

enter.place(x= 710, y= 70)

btn2.place(x=710, y=115)

btn3.place(x=710, y=145)

btn4.place(x=710, y=175)

btn5.place(x=710, y=205)

btn6.place(x=710, y=235)

btn7.place(x=710, y=265)

btn8.place(x=710, y=295)

btn9.place(x=710, y=325)

btn10.place(x = 710, y=355)

btnAmbareen.place(x=710, y=385)

btnAman.place(x=710, y=415)

tk.mainloop()
