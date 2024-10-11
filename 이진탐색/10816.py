from bisect import bisect_left, bisect_right

def countNumofCard(arr, card):
    left = bisect_left(arr, card)
    right = bisect_right(arr, card)
    
    return right - left
    

N = int(input())
table = list(map(int, input().split()))

M = int(input())
sang = list(map(int, input().split()))

table.sort()
for card in sang:
    print(countNumofCard(table, card), end=" ")
