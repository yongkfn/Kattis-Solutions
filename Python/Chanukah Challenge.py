P = int(input())

for i in range(P):
    K, N = map(int,input().split())
    sum = 0
    for i in range(N):
        sum += (N - i + 1)
    print(K, sum)
