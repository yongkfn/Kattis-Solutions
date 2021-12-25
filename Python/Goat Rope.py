from math import sqrt

x, y, x1, y1, x2, y2 = map(float,input().split())

if y > y2:
    if x > x2:
        d = sqrt((x-x2)**2+(y-y2)**2)
    elif x < x1:
        d = sqrt((x-x1)**2+(y-y2)**2)
    else:
        d = y-y2

elif(y<y2 and y>y1):
    if x < x1:
        d = x1-x
    else:
        d = x - x2

else:
    if x > x2:
        d = sqrt((x-x2)**2+(y-y1)**2)
    elif x < x1:
        d = sqrt((x-x1)**2+(y-y1)**2)
    else:
        d = min(y1-y,y2-y)

print(abs(d))
        
        
        
