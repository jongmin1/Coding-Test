A, B, C = list(map(int, input().split()))
if (C-B) == 0:
    t = -1
else:
    t = A // (C-B) + 1
if t < 1:
    t = -1
print(t)