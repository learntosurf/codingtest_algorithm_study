from collections import deque

queue = deque()
answer = []

a, b = map(int, input().split())

for i in range(1, a+1):
    queue.append(i)

while queue:
    for i in range(b-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")
