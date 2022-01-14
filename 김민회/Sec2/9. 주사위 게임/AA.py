
# 주사위 게임 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec2/9.주사위 게임/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 3개의 주사위 (눈 6까지) 
# 2. N명이 주사위 게임에 참가 
# 규칙 1) 같은 눈이 3개 >> 10,000 + 눈 * 1000 원의 상금 
# 규칙 2) 같은 눈이 2개 >> 1,000 + 눈 * 100 원의 상금 
# 규칙 3) 모두 다른 눈  >> 가장 큰 눈 * 100 원의 상금 
# 
# 3. 가장 많은 상금을 받은 사람의 상금을 출력 
# 
# 입력 1) N 
# 입력 2) N개 줄에 각 사람이 던진 주사위 눈 
#--------------------------------------------------------------------------------# 

N = int(input()) 

winner = 0 

for i in range(N):
    a, b, c = map(int, input().split()) 
    
    if a == b == c: 
        prize = 10000 + a * 1000 
    elif a==b | b==c: 
        prize = 1000 + b * 100 
    elif a==c: 
        prize = 1000 + a * 100 
    else:
        prize = max(a, b, c) * 100 
    
    if prize > winner:
        winner = prize 

print(winner) 
        




