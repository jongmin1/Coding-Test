import math

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

cntT = [] 
cntP = 0

for i in range(len(size)):
    cntT.append(math.ceil(size[i]/T))

print(sum(cntT))
print(N//P, N%P) 