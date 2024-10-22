N = int(input())
postfix = input().strip()
operator = ['+', '-', '*', '/']
operand = {}
for i in range(N):
    operand[chr(65+i)] = int(input())

stack = []
t = 0
for i in range(len(postfix)):
    if postfix[i] in operand :
        stack.append(operand[postfix[i]])
    else:
        if postfix[i] in operator:
            a = stack.pop()
            b = stack.pop()
            
            if postfix[i] == "+":
                t = b + a
            if postfix[i] == "-":
                t = b - a
            if postfix[i] == "*":
                t = b * a
            if postfix[i] == "/":
                t = b / a
            
            stack.append(t)
        else:
            stack.append(postfix[i])

print(round(stack[0], 2))
        