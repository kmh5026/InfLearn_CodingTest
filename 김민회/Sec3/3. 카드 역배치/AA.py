
# 카드 역배치 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/3. 카드 역배치/in5.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 기존) 1부터 20까지 적혀있고, 오름차순으로 나열된 카드들  (숫자와 순서가 일치) 
# 2. 역배치) 구간 [a, b]가 주어지면, 위치 a부터 위치 b까지의 카드를 역순으로 재배치 
# 3. 10개의 구간이 주어지면, 위 규칙에 따라 주어진 구간 순서대로 카드를 재배치하는 프로그램 작성 
# 
# 입력) 10개 줄에 거쳐 10개의 구간 입력  (a<=b, 1이상 20이하) 
# 출력) 마지막 카드들의 배치를 한 줄에 출력 
#--------------------------------------------------------------------------------# 

card = list(range(21))   # [0, 1, 2, ... , 19, 20] 

for trial in range(10): 
    a, b = map(int, input().split()) 
    tmp = card[ a : b+1 ] 
    tmp = tmp[::-1] 
    card[a : b+1] = tmp 

card = card[1:] 

for i in card: 
    print(i, end=' ')
    
