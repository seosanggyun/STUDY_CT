
## 정수 N과 정수 X 입력받기
N, X = map(int, input().split())

## 수열 A 입력받기
A = list(map(int, input().split()))

## A에서 X보다 작은 수를 출력하기 위해선
## list A를 하나하나 다 순회해봐야함
## for문으로 순회
for i in A:
    ## 근데 i가 X보다 작다?
    if i < X:
        ## i 출력하고 줄 바뀌면 안되니까 end=' '써서 한칸 띄움
        print(i, end=' ')