
# 격자판 회문수 ***** (소스코드와 다름) 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/11. 격자판 회문수/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 한자리 자연수로 채워진 7x7 격자판 
# 2. 가로방향 / 세로방향으로 길이 5짜리 회문수가 몇 개 있는지 출력하는 프로그램 작성 
# 3. 회문수 : 121처럼 앞에서 읽든 뒤에서 읽든 같은 숫자 
# 
# 입력1) 7 x 7 격자판 (7줄에 걸쳐) 
# 출력) 5자리 회문수 개수 
#--------------------------------------------------------------------------------# 

xx = [ list(map(int, input().split())) for _ in range(7) ] 

cnt = 0 

# 가로방향 
for i in range(7): 
    for j in range(3): 

        tmp = xx[i][j:j+5]   # 가로 방향으로 5개 slicing 
        if tmp == tmp[::-1]: 
            cnt += 1 
        
        tmp = []             # 세로 방향 
        for k in range(5): 
            tmp.append( xx[j+k][i] ) 
        if tmp == tmp[::-1]: 
            cnt += 1 

print(cnt) 


'''
# 소스코드 ***** 

board = [ list(map(int, input().split())) for _ in range(7) ]
cnt = 0 

for i in range(3):
    for j in range(7): 

        tmp = board[j][i:i+5]     # 가로방향 같으면 count 
        if tmp == tmp[::-1]: 
            cnt += 1 

        for k in range(2):        # 세로방향은 slicing 불가 
            if board[ i+k ][j] != board[ i+5 - (k+1) ][j]:   # 세로방향 다르면 for문 break 
                break 
        else:
            cnt += 1
        
print(cnt)




# <회문의 길이가 가변적일 때 코드> ***** 

board = [ list(map(int, input().split())) for _ in range(7) ] 

cnt=0 
len=5 

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+len]
        if tmp == tmp[::-1]:
            cnt += 1 

        #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다. 

        for k in range(len//2):    # *** 
            if board[ i+k ][j] != board[ i+len - (k+1) ][j]: 
                break 
        else:
            cnt += 1
        
print(cnt)
'''