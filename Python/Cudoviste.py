R, C = map(int,input().split())
carpark = [list(input()) for _ in range(R)]

a,b,c,d,e = 0,0,0,0,0

for i in range(R-1):
    for j in range(C-1):
        chars = carpark[i][j:j+2] + carpark[i+1][j:j+2]
        if '#' in chars: continue
        X_count = 0
        for char in chars:
            if 'X' in char:
                X_count += 1
        if X_count == 0:
            a += 1
        elif X_count == 1:
            b += 1
        elif X_count == 2:
            c += 1
        elif X_count == 3:
            d += 1
        elif X_count == 4:
            e += 1

print(f'{a}\n{b}\n{c}\n{d}\n{e}')
        
