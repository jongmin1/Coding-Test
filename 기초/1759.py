# 최대한 휴먼 에러 발생하지 않게 코드 작성하기 (알파벳 잘못 적거나 하는 등)
 
from itertools import combinations
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
alpha = list(input().strip().split())
gather = ['a','e','i','o','u']
answer = []
result = list(combinations(alpha, l))
for i in result:
    i = list(i)
    i.sort()
    count = 0
    for j in gather:
        if j in i:
            count += 1
    if 1 <= count <= l-2:
        pwd = ''.join(i)
        answer.append(pwd)
answer.sort()
for i in answer:
    print(i)