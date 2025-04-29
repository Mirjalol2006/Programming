import time
import random

n = int(input("Ro'yxatning elementlar sonini kiriting: "))
a = [0] * n
n = len(a)

for i in range(n):
    a[i] = random.randint(1,100)


def bubble_sort(a):      # pufakchali tartibalash
    for i in range(n):
        for j in range(i, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] 


def selection_sort(a):    # tanlash orqali tartiblash 
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


def insertion_sort(a):     # kiritish orqali tartiblash
    for i in range(1, n):
        v = a[i]
        j = i
        while j >= 1 and v < a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = v


def shell_sort(a):         # shell tartiblash
    h = 1
    while h <= n/3:
        h = h * 3 + 1
    while h > 0:
        for i in range(h, n):
            v = a[i]
            j = i
            while j > h-1 and a[j - h] >= v:
                a[j] = a[j - h]
                j -= h
            a[j] = v
        h //= 3


def time_(function, a):
    a_copy = a[:] 
    d = time.time()
    function(a_copy) 
    b = time.time()
    return b - d


bubble = time_(bubble_sort, a)
selection = time_(selection_sort, a)
insertion = time_(insertion_sort, a)
shell = time_(shell_sort, a)


print(f"Bubble Sort ishlash vaqti: {bubble:.6f} soniya")
print(f"Selection Sort ishlash vaqti: {selection:.6f} soniya")
print(f"Insertion Sort ishlash vaqti: {insertion:.6f} soniya")
print(f"Shell Sort ishlash vaqti: {shell:.6f} soniya")