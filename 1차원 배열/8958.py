# can be more simplified

n = int(input())
ox = []
for i in range(n):
    ox.append(input())

r = []
for i in range(n):
    score = 0
    pre = ''
    cnt = 1
    for c in ox[i]:
        if c == 'O':
            if c == pre:
                cnt += 1
            score += cnt
        else:
            cnt = 1
        pre = c
    r.append(score)

for i in range(n):
    print(r[i])