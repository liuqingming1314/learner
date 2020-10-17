def partition(li,left,right):
    tmp=li[left]
    while left<right:
        while left<right and tmp<=li[right]:
            right-=1
        li[left]=li[right]
        while left<right and tmp>=li[left]:
            left+=1
        li[right]=li[left]
    li[left]=tmp
    return left

def quick_sort(li,left,right):
    if left<right:
        mid=partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

li=[4,3,6,7,2,1,5,9,8]
quick_sort(li,0,len(li)-1)
print(li)