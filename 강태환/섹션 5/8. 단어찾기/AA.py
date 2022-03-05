import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
word = set()
yesw = set()
for _ in range(n):
    word.add(input())
for _ in range(n-1):
    yesw.add(input())
print(list(word - yesw)[0])