
# 단어찾기 (해쉬) *** (해시 개념문제)

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec5/8. 단어찾기/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 시를 쓰기 전에 쓰일 단어를 미리 노트에 적어둠 
# 2. N개의 단어들 중 시에 쓰지 않은 단어 하나를 찾는 프로그램 작성 
# 
# 입력1) N (3 이상 100 이하) 
# 입력2) 노트에 적어둔 N개의 단어 (N줄에 걸쳐) 
# 입력3) 시에 쓰인 N-1개의 단어 (N-1줄에 걸쳐) 
# 출력) 시에 쓰지 않은 1개 단어 
#--------------------------------------------------------------------------------# 

N = int(input()) 

note = {} 

for _ in range(N): 
    tmp = input() 
    note[tmp] = 1 

for _ in range(N-1): 
    word_used = input() 
    note[word_used] = 0 


# items: 키-값 쌍을 모두 가져옴   (리스트 안의 튜플 형태로) 
# keys: 키를 모두 가져옴         (리스트 형태) 
# values: 값을 모두 가져옴       (리스트 형태) 

# print(note.items()) 

for key, val in note.items(): 
    if val == 1: 
        print(key) 
        break 
