remainder = []
cnt = 0

for i in range(10):
    num = int(input())
    t = num % 42
    if not t in remainder:
        cnt += 1
        remainder.append(t)

print(cnt)