"""
def select_sort_simple(li):
    li_new=[]
    for i in range(len(li)):                      #时间复杂度o（n²）
        min_val=min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


li=[2,5,3,1,9,4,8,6,7]
print(select_sort_simple(li))
"""

def select_sort(li):
    for i in range(len(li)-1):          #第i趟
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                min_loc=j
        li[min_loc],li[i]=li[i],li[min_loc]
        print(li)

li=[2,5,3,1,9,4,8,6,7]
print(li)
select_sort(li)