from bisect import bisect_left

N = int(input())
l = list(map(int, input().split()))
com = l.copy()

sorted_unique_l = sorted(set(l))

r = []
for x in l:
    r.append(bisect_left(sorted_unique_l, x))

for i in r:
    print(i, end=" ")