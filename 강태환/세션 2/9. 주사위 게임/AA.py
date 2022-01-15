#이것도 도저히 시작을 못하겠어서 답지 봤읍니다
import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
win = 0
for i in range(n):
    dice = input().split()
    a, b, c = map(int, dice)
    if a == b == c:
        prz = a*1000 + 10000
    elif a == b or a == c:
        prz = a*100 + 1000
    elif b == c:
        prz = b*100 + 1000
    else:
        prz = max(a,b,c)*100
    if prz > win:
        win = prz
print(win)    
        