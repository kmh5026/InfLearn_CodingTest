
# 두 리스트 합치기 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec3/4. 두 리스트 합치기/in2.txt', 'rt')

#--------------------------------------------------------------------------------# 
# 1. 오름차순으로 정렬된 두 리스트 입력 
# 2. 두 리스트를 오름차순으로 합쳐 출력하는 프로그램 작성 
# 
# 입력1) 첫번째 리스트의 크기 N  (1이상 100이하) 
# 입력2) N개 리스트 원소 (오름차순) 
# 입력3) 두번째 리스트의 크기 M  (1이상 100이하) 
# 입력4) M개 리스트 원소 (오름차순) 
#--------------------------------------------------------------------------------# 


N = int(input()) 
list1 = list(map(int, input().split())) 

M = int(input()) 
list2 = list(map(int, input().split())) 

list3 = list1 + list2 

list3.sort() 

for i in list3:
    print(i, end=' ') 


'''
### 다른 방법 (소스코드)        
N = int(input()) 
list1 = list(map(int, input().split())) 

M = int(input()) 
list2 = list(map(int, input().split())) 

list3 = [] 

i1 = i2 = 0

while i1 < N and i2 < M: 
    if list1[i1] < list2[i2]:
        list3.append(list1[i1])
        i1 += 1 
    else:
        list3.append(list2[i2]) 
        i2 += 1 

# N과 M이 다르고, 두 리스트 중 어떤 리스트가 먼저 끝나는지 알 수 없음 
# >> i1 / i2를 N/M과 비교 
if i1 < N:
    list3 = list3 + list1[i1:] 

if i2 < M: 
    list3 = list3 + list2[i2:] 

for i in list3:
    print(i, end=' ') 
'''

