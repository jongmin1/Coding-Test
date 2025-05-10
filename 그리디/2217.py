# 로프
# 시도 횟수 : 1
# 참고 여부 : O
# 너무 오랜만에 풀어서 감 잡느라 시간 걸림.. 냅색 풀듯이 푸는 방법 생각 안 나서 참고함.
# 이번 그리디 문제 풀어보고 느낀 건, sort가 포인트인가? 

import sys
input = sys.stdin.readline

K = int(input())
ropes = [int(input().strip()) for _ in range(K)]

ropes.sort(reverse=True)

max_w = -1
for i in range(K):
    t = ropes[i] * (i+1)
    max_w = max(max_w, t)

print(max_w)