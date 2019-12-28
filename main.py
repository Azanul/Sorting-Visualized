from heap_sort import sort as HS
from insertion_sort import sort as IS
from merge_sort import sort as MS
from quick_sort import sort as QS
from radix_sort import sort as RS
from selection_sort import sort as SS
from OFA import *

SIZE=140
tk, canvas = create_canvas(SIZE+20)
tk.title("Sorting Visualized")

blocks=[]
generate(canvas, blocks, SIZE)
btn1 = Button(tk, text = 'Shuffle', bd = '5', command = lambda: shuffle(tk, canvas, blocks, SIZE))
btn2 = Button(tk, text = 'Insertion Sort', bd = '5', command = lambda: IS(tk, canvas, blocks))
btn3 = Button(tk, text = 'Selection Sort', bd = '5', command = lambda: SS(tk, canvas, blocks))
btn4 = Button(tk, text = 'Merge Sort', bd = '5', command = lambda: MS(tk, canvas, blocks))
btn5 = Button(tk, text = 'Quick Sort', bd = '5', command = lambda: QS(tk, canvas, blocks, SIZE-1))
btn6 = Button(tk, text = 'Heap Sort', bd = '5', command = lambda: HS(tk, canvas, blocks))
btn7 = Button(tk, text = 'Radix Sort', bd = '5', command = lambda: RS(tk, canvas, blocks))
btn1.place(x = 710, y = 5)
btn2.place(x = 710, y = 65)
btn3.place(x = 710, y = 95)
btn4.place(x = 710, y = 125)
btn5.place(x = 710, y = 155)
btn6.place(x = 710, y = 185)
btn7.place(x = 710, y = 215)
tk.mainloop()