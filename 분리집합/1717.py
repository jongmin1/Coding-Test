'''
시도 횟수 : 1
참고 여부 : O
처음 풀어보는 union find 문제
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find(x):
    if p[x] < 0:  # 음수면 루트 노드
        return x
    p[x] = find(p[x])  # 경로 압축
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    
    # 더 작은 값(더 큰 집합)이 부모가 되도록
    if p[a] > p[b]:  # p[a]가 더 크면 (= 집합 a가 더 작으면)
        a, b = b, a   # b가 더 큰 집합이므로 a와 b를 교환
    
    # 이 시점에서 p[a] <= p[b] 임이 보장됨
    p[a] += p[b]  # 음수끼리 더하므로 집합 크기가 증가
    p[b] = a      # b를 a의 자식으로

n, m = map(int, input().split())
p = [-1] * (n + 1)  # 음수값은 집합의 크기를 의미

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")