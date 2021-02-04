a = int(input())
b = int(input())
c = int(input())
r = a*b*c

l = str(r)
r = []
for i in range(10):
    r.append(0)

for c in l:
    r[int(c)] += 1

for i in range(10):
    print(r[i])

# result = list(str(a * b * c))
# for i in range(10):
#     print(result.count(str(i)))