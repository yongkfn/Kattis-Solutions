x,y = map(int,input().split())
print(int(str(x)[::-1])) if int(str(x)[::-1]) > int(str(y)[::-1]) else print(int(str(y)[::-1]))
