import sys
#sys.stdin = open('input.txt','rt')
n = input()
num = 0
for i in range(len(n)):
    if n[i].isnumeric() == True:
        num = num*10 + int(n[i])
cnt = 0
for i in range(1,num+1):
    if num%i == 0:
        cnt+=1
print(num, cnt, sep = '\n')