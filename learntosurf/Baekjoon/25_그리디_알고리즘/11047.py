N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True) # 내림차순 정렬
# coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

result = 0 
for coin in coins:
    result += K // coin 
    K = K % coin

print(result)
