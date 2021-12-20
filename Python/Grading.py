a, b, c, d, e = map(int,input().split())

score = int(input())

if a<score: print('A')
elif b<=score<a: print('B')
elif c<=score<b: print('C')
elif d<=score<c: print('D')
elif e<=score<d: print('E')
else: print('F')
                      
