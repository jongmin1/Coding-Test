'''
시도 횟수 : 1
참고 여부 : 세모
1717과 비슷해서 저거 참고함
'''

import sys
input = sys.stdin.readline

def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return -p[a]
    
    if p[a] > p[b]:
        a, b = b, a
    p[a] += p[b]
    p[b] = a
    return -p[a]

N, M = map(int, input().split())
planets = [int(input()) for _ in range(N)]

p = [-planets[i] for i in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())  
    print(union(a, b))