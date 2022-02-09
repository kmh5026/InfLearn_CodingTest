
# 스도쿠 검사 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/10. 스도쿠 검사/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 9 x 9 격자판 형식의 스도쿠 입력 (9줄) 
# 2. 완성된 스도쿠 입력되면 'YES'를 출력, 잘못 풀었으면 'NO'를 출력하는 프로그램 작성 
# 
# 입력1) 9 x 9 스도쿠 숫자 
# 출력) 맞았는지 틀렸는지 
#--------------------------------------------------------------------------------# 

xx = [ list(map(int, input().split())) for _ in range(9) ] 

def sudoku(xx): 
    # 가로 / 세로 
    for i in range(9): 
        row = [0] * 10 
        col = [0] * 10 
        for j in range(9): 
            row[ xx[i][j] ] = 1    # 가로 > 해당 숫자 등장한 경우에 1로 변경 (중복으로 등장해도 1로 그대로) 
            col[ xx[j][i] ] = 1    # 세로 > 해당 숫자 등장한 경우에 1로 변경 (중복으로 등장해도 1로 그대로) 
        if sum(row) < 9 or sum(col) < 9:
            return False 
    
    
    # 정방형 : 4중 for문 >>> 그룹 탐색 ***** 

    # (012 012) (012 345) (012 678) / (345 012) (345 345) (345 678) / (678 012) (678 345) (678 678) 
    for i in range(3): 
        for j in range(3):                # i,j = 총 9개의 그룹 
            square = [0] * 10 

            for k in range(3):            # k,l = 그룹 내 9개의 숫자 
                for l in range(3): 
                    square[ xx[i*3 + k][j*3 + l] ] = 1 
                    
            if sum(square) < 9: 
                return False 
    
    return True     # 모든 조건 만족 


if sudoku(xx): 
    print('YES') 
else: 
    print('NO') 
