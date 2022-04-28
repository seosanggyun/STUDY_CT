N, R, Q = map(int, input().split())

tree = [[] for _ in range(N + 1)]



for i in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

print(tree)

def countnode(x):
    





# print(Q_list)

# for i in range(N-1):
#     parent, child = arr[i*2], arr[i*2 + 1]
#     print(parent, child)

#     if tree[parent][0] == 0:
#         tree[parent][0] = child
#     else:
#         tree[parent][1] = child

#     tree[child][2] = parent

#     print(tree)