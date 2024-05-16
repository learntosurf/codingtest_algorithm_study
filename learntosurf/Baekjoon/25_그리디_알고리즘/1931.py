N = int(input())

meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0])) 

time = 0 
result = 0 
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        result += 1

print(result)
