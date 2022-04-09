
### 깊이 우선 탐색 

# 1. 전위순회 

def DFS(v): 
    if v > 7: 
        return 
    
    else: 
        print(v, end=' ')     ### 호출 넘어가기 전에 task 수행 >>> 전위순회 
        DFS(v*2)              # DFS(2) > DFS(2*2)   = DFS(4)    ( DFS(4*2)와 DFS(4*2+1)은 7 초과하므로 실행되지 않음 ) 
                              #        > DFS(2*2+1) = DFS(5)    ( DFS(5*2)와 DFS(5*2+1)은 7 초과하므로 실행되지 않음 ) 
        DFS(v*2+1)            # DFS(3) > DFS(3*2)   = DFS(6)    ( DFS(6*2)와 DFS(6*2+1)은 7 초과하므로 실행되지 않음 ) 
                              #        > DFS(3*2+1) = DFS(7)    ( DFS(7*2)와 DFS(7*2+1)은 7 초과하므로 실행되지 않음 ) 

if __name__ == '__main__': 
    DFS(1) 


# 2. 중위순회 

def DFS(v): 
    if v > 7: 
        return 
    
    else: 
        
        DFS(v*2)              # 
                              # 
                              
        print(v, end=' ')     ### 호출 중간에 task 수행 >>> 중위순회 (거의 없음) 
        
        DFS(v*2+1)            # 
                              # 


if __name__ == '__main__': 
    DFS(1) 


# 3. 후위순회 

def DFS(v): 
    if v > 7: 
        return 
    
    else: 
        
        DFS(v*2)              # 
                              # 
        
        DFS(v*2+1)            # 
                              # 
                                      
        print(v, end=' ')     ### 호출 끝나고 task 수행 >>> 후위순회 (병합정렬 시 사용) 


if __name__ == '__main__': 
    DFS(1) 
