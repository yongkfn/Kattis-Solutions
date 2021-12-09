import math

N = int(input())

for i in range(N):
    v, t, x, h1, h2 = map(float, input().split())
    time = x/(v*math.cos(t*(math.pi/180)))  
    if(v*time*math.sin(t*(math.pi/180)) - (0.5*9.81*(time**2))) >= (h1 + 1) and (v*time*math.sin(t*(math.pi/180)) - (0.5*9.81*(time**2))) <= h2 - 1:
        print('Safe')
    else: print('Not Safe')
