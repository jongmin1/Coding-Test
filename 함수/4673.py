def solve(a):
    r = 0
    for i in str(a):
        r += int(i)
    return r + a

u = set(range(1, 10001))
remove = set()

for i in u:
    i = solve(i)
    remove.add(i)

self  = u - remove
for i in sorted(self):
    print(i)