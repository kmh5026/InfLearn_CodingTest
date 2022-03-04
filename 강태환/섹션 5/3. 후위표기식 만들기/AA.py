import sys
#sys.stdin=open("input.txt", "r")
n = input()
stack = []
con = ''
for x in n:
    if x.isnumeric():
        con += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                con += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                con += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                con += stack.pop()
            stack.pop()
while stack:
    con += stack.pop()
print(con)