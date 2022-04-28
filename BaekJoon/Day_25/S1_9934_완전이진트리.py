

# 중위순회의 순서가 주어질 때 트리를 만들어야 함

# 어차피 노드의 개수가  2**K - 1 개로 고정이니까
# 배열의 중간값이 최상위 노드임
# 제발 문제 좀 읽어라


K = int(input())

arr = list(map(int, input().split()))

tree = [[] for _ in range(K)]

# DFS를 이용해서 
# 중간값을 계속해서 찾아가는 함수

def binary_mid(start, end, level):

    # 계속 반씩 쪼개 내려가다가 다 내려가서 더 쪼갤 수 없을 때
    # 그 값이 해당 레벨의 맨 왼쪽 노드임
    if start == end:
        tree[level].append(arr[start])
        return
    
    # 반씩 쪼개 내려감
    mid = (start + end) // 2
    # 해당 레벨의 중간 값을 트리에 저장
    tree[level].append(arr[mid])

    # 왼쪽부터 중간값 탐색해주고
    # 깊게 내려갈수록 level에 +1 해줌
    binary_mid(start, mid-1, level+1)
    binary_mid(mid+1, end, level+1)

# 시작점은 0, 끝점은 배열길이 -1, 처음 레벨은 0 
binary_mid(0, len(arr)-1, 0)


for k in range(K):
    print(*tree[k])
# print(tree)
