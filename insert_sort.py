def insert_sort(li):
    for i in range(1,len(li)):
        tmp=li[i]                  #i是摸到牌的下标
        j=i-1                      #j是手里牌的下标
        while j>=0 and li[j]>tmp:
            li[j+1]=li[j]
            j-=1
        li[j+1]=tmp
        print(li)

li=[3,6,8,4,5,1,9,2,7]
print(li)
insert_sort(li)
