N = int(input())

i = 1
boundary = 2
while N >= boundary:
    boundary += 6*i
    i += 1
print(i)