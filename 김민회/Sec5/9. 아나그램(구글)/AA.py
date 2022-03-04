
# 아나그램 (구글) ***** 

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/9. 아나그램(구글)/in4.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 아나그램 (Anagram) : 알파벳 나열 순서는 달라도 구성이 일치하면 두 단어는 아나그램 
# 2. 알파벳과 그 개수가 모두 일치하는 경우 
# 3. 길이가 같은 두 단어가 주어지면 아나그램인지 판별하는 프로그램 작성 
# 
# 입력1) 첫번째 단어 
# 입력2) 두번째 단어 
# 출력) 'YES' / 'NO' 
#--------------------------------------------------------------------------------# 

word1 = input() 
word2 = input() 

anagram = {} 

for i in word1: 
    # 새로운 단어 > count 
    if i not in anagram: 
        anagram[i] = 1 
    # 중복된 단어 > count 
    else: 
        anagram[i] += 1     # 결국 val들은 각 첨자의 등장 횟수를 나타냄 

for j in word2: 
    if j in word1:          # 등장 횟수 일치하는지 판별하기 위해 역으로 count 
        anagram[j] -= 1


### 아나그램 해시 테이블의 값들만 뽑음 
check = anagram.values() 

for k in check: 
    # 구성이 하나라도 다른게 나오면 'NO' 
    if k != 0: 
        print('NO') 
        break 
# 구성이 다 같으면 (모두 0) 'YES' 
else: 
    print('YES') 





### 소스코드 : .get( ) 활용 
'''
for i in word1: 
    anagram[i] = anagram.get(i, 0) + 1 

for j in word2: 
    anagram[j] = anagram.get(j, 0) - 1 


for k in word1: 
    # 구성이 하나라도 다른게 나오면 'NO' 
    if anagram.get(k) > 0: 
        print('NO') 
        break 
# 구성이 다 같으면 (모두 0) 'YES' 
else: 
    print('YES') 
''' 