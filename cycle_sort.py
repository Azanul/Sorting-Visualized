
from OFA import *

def sort(list = blocks):
    for b in list:
        print(b.h, end = " ")
    print()
    writes = 0
    LS = len(list)

    for i in range(LS):
        item = list[i]
        pos = i
        for j in range(i + 1, LS):
            if list[j].h < item.h:
                pos += 1
        if pos == i:
            continue

        while item == list[pos]:
            pos += 1


        swap(pos, i, list)
        writes += 1


        while pos != i:

         pos = i

         for j in range(i + 1, LS):
             if list[j].h < item.h:
                 pos += 1

         while item == list[pos]:
             pos += 1

         # list[pos], item = item, list[pos]
         swap(pos, i, list)
         writes += 1
    for b in list:
        print(b.h, end = " ")
    print()

if __name__ == "__main__":
    tk.title("Cycle Sort")
    generate()
    btn1 = Button(tk, text='Shuffle', bd='5', command=lambda: shuffle())
    btn2 = Button(tk, text='Sort', bd='5', command=lambda: sort())
    btn1.pack(side='left')
    btn2.pack(side='left')
    tk.mainloop()

