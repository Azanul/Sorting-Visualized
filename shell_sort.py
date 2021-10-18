from OFA import *

def sort(list=blocks):
    LS = len(list)
    gap = LS // 2
    while gap > 0:
        for i in range(gap, LS):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap].h > temp.h:
                swap(j, j-gap, list)
                j -= gap
        gap //= 2

if __name__ == "__main__":
    tk, canvas = create_canvas()
    tk.title("Shell Sort")
    generate()
    btn1 = Button(tk, text='Shuffle', bd='5', command=lambda: shuffle())
    btn2 = Button(tk, text='Sort', bd='5', command=sort())
    btn1.pack(side='left')
    btn2.pack(side='left')
    tk.mainloop()
