import sys
input = sys.stdin.readline

N, T = map(int, input().split())

memo = dict()

for i in range(N):
    s, p = map(str, input().strip().split())
    memo[s] = p

for i in range(T):
    s = input().strip()
    print(memo[s])
