import sys
input = sys.stdin.readline

N = int(input())
cols = [[i, 0] for i in range(1001)]
start = 1000
end = -1
maxHeight, maxHeightPos = 0, 0
for i in range(N):
    a, b = map(int, input().split())
    cols[a][1] = b
    if start > a:
        start = a
    if end < a:
        end = a
    if maxHeight < b:
        maxHeight = b
        maxHeightPos = a

h = 0
area = maxHeight       
for i in range(start, maxHeightPos):
    h = max(h, cols[i][1])
    area += h

h = 0
for i in range(end, maxHeightPos, -1):
    h = max(h, cols[i][1])
    area += h
    
'''
d = 0
area = maxHeight   
h = cols[start][1]     
for i in range(start, maxHeightPos+1):
    if cols[i][1] >= h: 
        d = i - start
        area += d * h
        h = cols[i][1]
        start = i

h = cols[end][1] 
for i in range(end, maxHeightPos-1, -1):
    if cols[i][1] >= h:
        d = end - i
        area += d * h
        h = cols[i][1]
        end = i
'''

print(area)



