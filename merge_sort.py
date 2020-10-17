# 牛逼三人组之--归并排序

def merge(li,low,mid,high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    #while执行完，两部分有部分肯定没数
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
    li[low:high+1] = ltmp

#li = [2,4,3,8,7,5,6,1]
#merge(li,0,3,7)
#print(li)
def merge_sort(li,low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

#li = list(range(1000))
#import random
#random.shuffle(li)
#print(li)
#merge_sort(li,0,len(li)-1)
#print(li)

def merge_sort_test(li,low,high):
    if low < high:                  
        mid = (low + high) // 2
        merge_sort_test(li,low,mid)
        merge_sort_test(li,mid+1,high)
        print(li[low:high+1])

li = list(range(10))
import random
random.shuffle(li)
print(li)
merge_sort_test(li,0,len(li)-1)
print(li)