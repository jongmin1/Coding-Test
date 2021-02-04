n = int(input())
pct = []

for i in range(n):
    cnt = 0 
    s = list(map(int, input().split()))
    avg = sum(s[1:])/s[0]
    for one in s[1:]:
        if one > avg:
            cnt += 1
    pct.append(cnt/s[0]*100)

for i in range(n):
    print(f'{pct[i]:.3f}%')

