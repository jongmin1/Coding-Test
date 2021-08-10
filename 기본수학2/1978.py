def check_prime(n):
    if n == 1:
        return 0
    if n in [2, 3, 5, 7]:
        return 1
    if n%10 not in [1, 3, 7, 9]:
        return 0
    for i in range(2, n):
        if n%i == 0:
            return 0
    return 1


len = input()
list_num = list(map(int, input().split()))
cnt = 0
for num in list_num:
    r = check_prime(num)
    if r == 1:
        cnt += 1
print(cnt)