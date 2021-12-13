N = int(input())

for i in range(N):
    p = input()
    l = len(p)
    for j in range(1, l + 1): #1 base
        if p == (p[0:j] * (int(l//j)+1))[0:l]:
            print(j)
            break

    
