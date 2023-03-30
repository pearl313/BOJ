import sys
input = sys.stdin.readline

def preorder(n):
    global ans
    if n != '.':
        ans += n
        preorder(tree[n][0])
        preorder(tree[n][1])

def inorder(n):
    global ans
    if n != '.':
        inorder(tree[n][0])
        ans += n
        inorder(tree[n][1])

def postorder(n):
    global ans
    if n != '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        ans += n

N = int(input())
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]

ans = ''
preorder('A')
print(ans)
ans = ''
inorder('A')
print(ans)
ans = ''
postorder('A')
print(ans)