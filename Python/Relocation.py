N, Q = map(int,input().split())
companies = list(map(int,input().split()))

for i in range(Q):
    a, b, c = map(int,input().split())
    if a == 1:
        companies[b-1] = c
    else:
        print(abs(companies[b-1]-companies[c-1]))
