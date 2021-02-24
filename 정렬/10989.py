# First,
# numsList = []
# n = int(input())
# for i in range(n):
#     numsList.append(int(input()))

# cntList = [0 for i in range(max(numsList)+1)]
# rList = [0 for i in range(n)]

# for i in numsList:
#     cntList[i] += 1

# t = 0
# for i in range(len(cntList)):
#     t += cntList[i]
#     cntList[i] = t

# for i in numsList:
#     rList[cntList[i]-1] = i
#     cntList[i] -= 1

# for i in rList:
#     print(i)

# Second,
# N = int(input())
# cntList = [0 for i in range(10001)]
# for i in range(N):
#     cntList[int(input())] += 1
# for i in range(10001):
#     while cntList[i]:
#         print(i)
#         cntList[i] -= 1

# Third,
import sys
N = int(sys.stdin.readline())
cntList = [0 for i in range(10001)]
for i in range(N):
    cntList[int(sys.stdin.readline())] += 1
for i in range(10001):
    while cntList[i]:
        print(i)
        cntList[i] -= 1
