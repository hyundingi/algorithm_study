# 배열로 표현한 이진 트리
tree = [node for node in range(16)]

# 2번 노드 확인
node = 2

# 2번 노드의 왼쪽 자식은 *2에 있다
print(tree[node * 2])

# 2번 노드의 오른쪽 자식은 *2 +1에 있다.
print(tree[node * 2 + 1])


# 10번 노드의 부모는
node = 10
print(tree[node // 2])

# 현재 노드와 전체 트리
def inorder(node, tree):
    # 현재 노드가 존재하는지 파악
    # 나의 노드가 트리보다 작은지
    if node < len(tree):
        # LVR - 중위 순회
        inorder(node * 2, tree)          # 먼저 왼쪽을 간다.
        print(tree[node], end=' ')        # 그 다음 나를 방문
        inorder(node * 2 + 1, tree)      # 마지막 오른쪽 방문

def preorder(node, tree):
    # 현재 노드가 존재하는지 파악
    # 나의 노드가 트리보다 작은지
    if node < len(tree):
        # VLR - 전위 순회
        print(tree[node], end=' ')          # 먼저 나를 방문
        preorder(node * 2, tree)            # 왼쪽 방문
        preorder(node * 2 + 1, tree)        # 마지막 오른쪽 방문

def postorder(node, tree):
    # 현재 노드가 존재하는지 파악
    # 나의 노드가 트리보다 작은지
    if node < len(tree):        # LRV - 후위 순회
        postorder(node * 2, tree)            # 먼저 왼쪽을 간다.
        postorder(node * 2 + 1, tree)        # 오른쪽 방문
        print(tree[node], end=' ')          # 마지막 나를 방문

inorder(1, tree)
print()
preorder(1, tree)
print()
postorder(1, tree)
print()