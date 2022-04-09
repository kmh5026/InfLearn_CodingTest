
# 재귀함수를 이용한 이진수 출력 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec6/1. 재귀함수란(이진수출력)/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 10진수 N이 입력 
# 2. 2진수로 변환하여 출력하는 프로그램 (재귀함수 이용) 
# 
# 입력) N (1 이상 1000 이하) 
# 출력) 이진수 
#--------------------------------------------------------------------------------# 

def DFS(x): 
    if x == 0:      # 함수 종료 (무한반복 방지) 
        return 
    
    else:           # 재귀함수 호출 
        DFS(x//2) 
        print(x%2, end='') 
        
# ex1) N = 11 
# DFS(11)  >  11 기록 (스택)  >  DFS(5) 
# DFS(5)   >   5 기록 (스택)  >  DFS(2) 
# DFS(2)   >   2 기록 (스택)  >  DFS(1) 
# DFS(1)   >   1 기록 (스택)  >  DFS(0)  > 함수 종료 
# print( 1%2 ) == print( 1 ) 
# print( 2%2 ) == print( 0 ) 
# print( 5%2 ) == print( 1 ) 
# print( 11%2 ) == print( 1 )  >>> 1011 출력 

# ex2) N = 23 
# DFS(23)  >  23 기록 (스택)  >  DFS(11) 
# DFS(11)   >   11 기록 (스택)  >  DFS(5) 
# DFS(5)   >   5 기록 (스택)  >  DFS(2) 
# DFS(2)   >   2 기록 (스택)  >  DFS(1) 
# DFS(1)   >   1 기록 (스택)  >  DFS(0)  > 함수 종료 
# print( 1%2 ) == print( 1 ) 
# print( 2%2 ) == print( 0 ) 
# print( 5%2 ) == print( 1 ) 
# print( 11%2 ) == print( 1 ) 
# print( 23%2 ) == print( 1 )  >>> 10111 출력 


if __name__ == '__main__': 
    N = int(input()) 
    DFS(N) 


'''
def ejin(x): 
    ans = '' 
    while x > 0: 
        div = x//2 
        mod = x%2 
        ans += str(mod) 
        x = div 
    print( ans[::-1] ) 

ejin(int(input())) 
'''