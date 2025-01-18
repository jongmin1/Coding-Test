import sys
input = sys.stdin.readline

N = int(input())

if N < 100:
    ans = N
else:    
    ans = 0
    for i in range(100, N+1):
        num = str(i)
        valid = True
        diff = int(num[0]) - int(num[1])
        for j in range(1, len(num)-1):
            if int(num[j]) - int(num[j+1]) != diff:
                valid = False
                break
        if valid:
            ans += 1
    ans += 99
print(ans)
    
