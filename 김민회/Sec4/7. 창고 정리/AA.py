
# 창고 정리 (그리디) *** 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec4/7. 창고 정리/in4.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 가로 길이 L인 창고의 상자 높이 조정 > 가장 높은 곳의 상자를 가장 낮은 곳으로 
# 2. 높은 곳 / 낮은 곳이 여러개면 아무거나 선택 
# 3. M회의 높이 조정 후 가장 높은 곳과 낮은 곳의 차이를 출력하는 프로그램 
# 
# 입력1) L (1 이상 100 이하) 
# 입력2) L개의 자연수 한 줄에 (공백) (100 이하) 
# 입력3) M (1 이상 1000 이하) 
# 출력) 가장 높은 곳과 가장 낮은 곳의 차이
#--------------------------------------------------------------------------------# 

L = int(input()) 

warehouse = list(map(int, input().split())) 

M = int(input()) 

warehouse.sort(reverse=True) 

# ex) 
# 87 81 76 76 69 68 65 42 40 14 

for _ in range(M): 
    warehouse[0] -= 1 
    warehouse[L-1] += 1 
    warehouse.sort(reverse=True) 

print( warehouse[0] - warehouse[L-1] ) 
