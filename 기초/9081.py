import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())

def nextOrder(s):
    a = -1
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            a = i
    if a == -1:
        print("".join(s))
        return
    
    b = -1
    for i in range(len(s)-1, a, -1):
        if s[a] < s[i]:
            b = i
            break
    
    s = list(s)
    s[a], s[b] = s[b], s[a]
    
    s = s[:a+1] + s[a+1:][::-1]
    
    print("".join(s))
            

for i in range(N):
    string = input().strip()
    nextOrder(string)
    
