
# 뮤직비디오 (결정 알고리즘) *****

'''
# 결정 알고리즘의 특징 
: 특정 범위 안에 답이 있다 
: 중간 지점 / 좌한 / 우한 설정 >> 이분탐색 
'''

import sys 
sys.stdin = open('/Users/kimmh/Desktop/Algorithm/Sec4/3. 뮤직비디오/in5.txt', 'rt') 

#--------------------------------------------------------------------------------# 
# 1. 총 N개의 곡을 M개의 dvd에 (각 dvd는 같은 크기, dvd 크기 최소화) 
# 2. 노래 순서는 그대로 
# 3. 한 노래를 쪼갤 수 없음 
# 
# 입력1) N, M (N은 1000 이하 자연수, M은 N 이하 자연수) 
# 입력2) 한 줄에 각 N개 곡의 길이(분) (10000분 이하) 
# 출력) dvd 최소 용량 크기 
#--------------------------------------------------------------------------------# 

N, M = map(int, input().split()) 

songs = list(map(int, input().split())) 


lt = max(songs)     # 용량 좌한 = 최소 1곡 
rt = sum(songs)     # 용량 우한 = 한 dvd 안에 모든 곡 


### 주어진 크기에 대한 DVD 개수 
def Count(dvd_len): 
    cnt = 1             # dvd 개수 초기화 
    len_sum = 0         # dvd 용량 초기화 

    for i in songs: 
        if len_sum + i > dvd_len:  # DVD 용량 초과할 경우 
            cnt += 1 
            len_sum = i            # 초과되게 만든 곡을 새 dvd에 녹음 
        
        else:                      # DVD 용량 초과되기 전까진 
            len_sum += i           # 계속 해당 dvd에 녹음 

    return cnt                     # 다 녹음된 후 DVD 갯수 


while lt <= rt:                    # dvd 최소용량 지점 
    mid = (lt + rt) // 2 

    if Count(mid) <= M:             # 녹음 후 DVD 개수가 M 이하일 때 (문제 만족)
        result = mid                # 일단 해당 용량 저장 
        rt = mid - 1                # 용량 줄여나가는 방향으로 

    else: # elif Count(mid) > M:    # DVD 개수가 M을 초과할 때 (불만족) 
        lt = mid + 1                # 용량 늘리는 방향으로 

print(result) 

