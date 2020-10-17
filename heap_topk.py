def sift(li,low,high):
    i=low    #i 最开始指向根节点
    j=2*i+1  #j 开始是左孩子
    tmp=li[low] #把堆顶存起来
    while j<=high:    #只要j位置有数
        if j+1<=high and li[j+1]<li[j]:    #如果有右孩子并且比较大
            j=j+1        #j指向右孩子
        if li[j]<tmp:    #j>low,给low往下降级
            li[i]=li[j]  #j占low位置
            i=j          #根节点向下一层
            j=i*2+1
        else:            #tmp大，low不用再降级
            break
        li[i]=tmp        #tmp放叶子结点上，位置没变

def topk(li,k):
    heap=li[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    for i in range(k,len(li)-1):
        if li[i]>heap[0]:
            heap[0]=li[i]
            sift(heap,0,k-1)

    for i in range(k-1,-1,-1):
        #i指向堆的最后一个元素
        heap[0],heap[i]=heap[i],heap[0]
        sift(heap,0,i-1)
    return heap


import random
li=list(range(1000))
random.shuffle(li)

print(topk(li,10))
