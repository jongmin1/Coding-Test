import sys
input = sys.stdin.readline

while True:
    string = input().rstrip('\n')
    
    if not string:
        break
    
    small, capital, num, space = 0, 0, 0, 0
    
    for i in range(len(string)):
        if string[i].islower():
            small += 1
        elif string[i].isupper():
            capital += 1
        elif string[i].isdigit():
            num += 1
        elif string[i] == " ":
            space += 1

    print(small, capital, num, space)