N = int(input())
count = 0
temp = list(map(int,input().split()))

for i in range(N):
    if temp[i] < 0:
        count += 1
print(count)
