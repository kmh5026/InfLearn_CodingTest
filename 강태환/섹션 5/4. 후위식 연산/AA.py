import sys
#sys.stdin=open("input.txt", "r")
n = input()
stack = []
for x in n:
    if x.isnumeric():
        stack.append(int(x))
    else:
        if x == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a*b))
        elif x == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a/b))
        elif x == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a+b))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a-b))
print(stack[0])