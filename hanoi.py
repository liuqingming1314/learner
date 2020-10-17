#汉诺塔问题
#n个盘子时：
#第一步：把n-1个盘子从A经过C移动到B
#第二步：把第n个盘子从A移动到C
#第三步：把n-1个盘子从B经过A移动到C
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s" % (a,c))
        hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")