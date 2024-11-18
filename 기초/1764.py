# 집합 사용법 익히기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = {input().strip() for _ in range(N)}
b = {input().strip() for _ in range(M)}

db = d & b
        
ans = sorted(db)
print(len(ans))
for i in ans:
    print(i)
