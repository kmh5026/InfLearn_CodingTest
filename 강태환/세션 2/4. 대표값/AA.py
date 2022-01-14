import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
a = list(map(int, input().split()))
mean = int((sum(a)/n) + 0.5)
min = 101
for num, scr in enumerate(a):
    abscr = abs(scr-mean)
    if abscr < min:
        min = abscr
        score = scr
        number = num+1
    elif min == abscr:
        if score < scr:
            score = scr
            number = num+1
print(score, number)        