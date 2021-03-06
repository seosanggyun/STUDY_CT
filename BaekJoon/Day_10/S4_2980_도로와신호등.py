## 어케 풀었냐

## 신호등의 개수와 도로 길이 입력
N, L = map(int, (input().split()))

## 상근이 트럭의현재 위치를 저장할 P,
## 상근이가 도로의 끝까지 이동하는데 걸린 시간을 저장할 T
P = 0
T = 0

## 신호등의 개수만큼 반복
for info in range(N):
    ## 신호등 정보 입력
    D, R, G = map(int, (input().split()))
    
    ## 상근이는 1초에 1미터 움직이므로
    ## 신호등 까지 도달하기 위해 움직인 거리가
    ## 곧 걸린 시간이므로
    ## 걸린 시간에 신호등 위치 - 현재 위치 더해줌
    T += D - P
    ## 현재 위치에 신호등 위치 - 현재 위치 더해줌
    P += D - P

    ## R + G가 신호등 한 싸이클인데
    ## 걸린시간을 한 싸이클로 나눈 나머지값을 TC에 저장
    TC = T % (R + G) 

    ## 만약에 TC의 값이 빨간불 지속시간보다 작다면
    if TC < R:
        ## 상근이의 트럭은 빨간불 지속시간이 끝날 때 까지
        ## 신호등에서 대기해야 하므로
        ## 걸린 시간에 빨간불 지속시간 - TC 더해줌
        T += R - TC

## 모든 신호등을 통과한 뒤
## 거리 끝까지 가야 하므로
## 거리 길이 - 현재 위치의 값을
## 걸린 시간에 더해줌
T += L - P
print(T)    

        
    