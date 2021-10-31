from OFA import *


def insertionSort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and up.h < bucket[j].h:
            swap(j + 1, j, bucket)
            j = j - 1
        bucket[j + 1] = up


def sort(list=blocks):
    copy_list = list[:]
    size = len(list) + 1
    bucket_size = (size - 1) // 5
    bucket_map = [i*bucket_size for i in range(5)]

    for j in copy_list:
        index_bucket = (j.h - 5) // size
        insert(bucket_map[index_bucket], j, list)
        bucket_map[index_bucket] += 1
    for i in range(5):
        insertionSort(list[i * 28:(i + 1) * 28])


if __name__ == "__main__":
    tk, canvas = create_canvas()
    tk.title("Bucket Sort")
    generate()
    btn1 = Button(tk, text='Shuffle', bd='5', command=lambda: shuffle())
    btn2 = Button(tk, text='Sort', bd='5', command=sort())
    btn1.pack(side='left')
    btn2.pack(side='left')
    tk.mainloop()
