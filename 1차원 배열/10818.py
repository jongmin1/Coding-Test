n = int(input())

itgs = input()
itgs = list(map(int, itgs.split()))

print('{} {}'.format(min(itgs), max(itgs)))