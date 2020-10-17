def sift(li,low,high):
    """
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i=low    #i 最开始指向根节点
    j=2*i+1  #j 开始是左孩子
    tmp=li[low] #把堆顶存起来
    while j<=high:    #只要j位置有数
        if j+1<=high and li[j+1]>li[j]:    #如果有右孩子并且比较大
            j=j+1        #j指向右孩子
        if li[j]>tmp:    #j>low,给low往下降级
            li[i]=li[j]  #j占low位置
            i=j          #根节点向下一层
            j=i*2+1
        else:            #tmp大，low不用再降级
            li[i]=tmp    #把tmp放某一级位置
            break
    else:
        li[i]=tmp        #tmp放叶子结点上，位置没变


def heap_sort(li):
    n=len(li)
    for i in range((n-1-1)//2,-1,-1):  #最后元素下标是n—1即孩子下标，父下标是孩子下标减一整除二
        sift(li,i,n-1)                 #i代表调整的根的部分下标
    #建堆完成
    for i in range(n-1,-1,-1):
        #i指向堆的最后一个元素
        li[0],li[i]=li[i],li[0]
        sift(li,0,i-1)


li=[i for i in range(100)]
import random
random.shuffle(li)
print(li)

heap_sort(li)
print(li)
