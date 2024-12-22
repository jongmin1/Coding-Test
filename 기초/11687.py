import sys
input = sys.stdin.readline

def countZero(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros

M = int(input())

left = 1
right = M * 5
rst = -1

while left <= right:
    mid = (left + right) // 2

    numZero = countZero(mid)

    if numZero < M:
        left = mid + 1
    else:
        if numZero == M:
            rst = mid
        right = mid - 1

print(rst)