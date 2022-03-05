import sys
#sys.stdin=open("input.txt", "r")
tmp = input()
p = dict()
for x in tmp:
    p[x] = p.get(x,0)+1
tmp = input()
for x in tmp:
    p[x] = p.get(x,0)-1
for key in p:
    if p.get(key) != 0:
        print('NO')
        break
else:
    print('YES')