'''
시도 횟수 : 1
참고 여부 : X
'''
import sys
input = sys.stdin.readline

string = input().strip()
N = len(string)
ans = set()
for i in range(1, N+1):
    for j in range(N - i + 1):
        ans.add(string[j:j+i])
print(len(ans))


''' 최적화 가능
import sys
input = sys.stdin.readline

s = input().strip()
N = len(s)
ans = set()

# 슬라이싱 대신 인덱스 직접 사용
for i in range(N):
    temp = []
    for j in range(i, N):
        temp.append(s[j])
        ans.add(''.join(temp))
        
print(len(ans))
'''