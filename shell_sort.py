#希尔排序

def insert_sort_gap(li,gap):         #gap是间隔
    for i in range(gap,len(li)):
        tmp = li[i]                  #i是摸到牌的下标
        j = i - gap                     #j是手里牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li,d)
        d //= 2

li = list(range(1000))
import random
random.shuffle(li)
shell_sort(li)
print(li)