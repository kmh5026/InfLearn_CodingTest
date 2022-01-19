# 첫번째 방법 #
'''
import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
for i in range(n):
    word = input()
    word = word.upper()
    if word == word[::-1]:
        print('#%d YES' %(i+1))
    else:
        print('#%d NO' %(i+1))
'''
# 두번째 방법 #
import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
for i in range(n):
    word = input()
    word = word.upper()
    for j in range(len(word)//2):
        if word[j] != word[-j-1]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' %(i+1))