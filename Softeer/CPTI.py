import sys
input =sys.stdin.readline

N, M = map(int, input().strip().split())

print(N, M)
# 최대 두가지 영역에서 서로 다르면 
# 다른 개수 <= 2 -> 친밀감 느낌 (ans에 추가)
ans = []
arr = []
for i in range(N):
    arr.append(input())

print(arr)