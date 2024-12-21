# brute force -> all cases
N = int(input())
temp = []
cal = 0
r = 0

for i in range(1, N+1):
    temp = list(map(int, str(i)))
    cal = i + sum(temp)
    if cal == N:
        r = i
        break

print(r)