N = int(input()) # 도시의 개수 
km = list(map(int, input().split())) # 도시 사이의 거리 
price = list(map(int, input().split())) # 리터당 가격

min_price = price[0]
total = 0

for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]
    total += min_price * km[i]
    
print(total)
