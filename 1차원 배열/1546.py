n = int(input())
s = list(map(int, input().split()))

new_s = [num*100/max(s) for num in s]

print(sum(new_s)/n)