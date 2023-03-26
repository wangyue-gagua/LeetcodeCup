""" 第一行两个整数n和m，表示小美的巧克力数量和小美的询问数量。

第二行n个整数a1,a2,...,an，表示n块正方形巧克力板的边长。注意你不能将巧克力板进行拆分。

第三行m个整数q1,q2,...,qm，第 i 个整数qi表示询问：如果小美选择一个能装qi重量的包，最多能装多少块巧克力板？（不考虑体积影响，我们认为只要质量满足要求，巧克力板总能塞进包里）

1≤n,m≤50000,1≤ai≤104,1≤qi≤1018 """

firstLine = input().split()
n = int(firstLine[0])
m = int(firstLine[1])
chockLenArr = [int(i) for i in input().split()]
query = [int(i) for i in input().split()]

# chockLenArr[i]表示第i块正方形巧克力板的边长 重量为边长的平方
# query[i]表示该背包能装的最大重量
# 问背包最多能装多少块巧克力板

# 首先将巧克力板排序，由小到大
chockLenArr.sort()

# 预处理表示前i块巧克力板的重量和
chockWeightSum = [0] * (n + 1)
for i in range(1, n + 1):
    chockWeightSum[i] = chockWeightSum[i - 1] + chockLenArr[i - 1] ** 2

# 二分查找
res = []
for i in range(m):
    left = 0
    right = n
    while left < right:
        mid = (left + right + 1) // 2
        if chockWeightSum[mid] <= query[i]:
            left = mid
        else:
            right = mid - 1
    res.append(left)

print(" ".join([str(i) for i in res]))