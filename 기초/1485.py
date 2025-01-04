'''
시도 횟수 : 2
참고 여부 : O
정사각형의 정의 -> 문제에서 말하는 것에 대한 정의부터 생각하기
'''

import sys
input = sys.stdin.readline

def cal(a, b):
    return (abs(b[0]-a[0])**2 + abs(b[1]-a[1])**2)

T = int(input())

for _ in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    
    arr.sort(key = lambda x : [x[0], x[1]])
    
    # 정사각형 -> 네개의 변과 두 대각선의 길이가 같아야 함함
    a = cal(arr[3], arr[1])
    b = cal(arr[3], arr[2])
    c = cal(arr[2], arr[0])
    d = cal(arr[1], arr[0])
    
    e = cal(arr[0], arr[3])
    f = cal(arr[1], arr[2])
    
    if a == b and b == c and c == d and d == a and e == f:
        print(1)
    else:
        print(0)