P, N = map(int,input().split())
parts = []

for i in range(N):
    parts.append(input())
    if len(set(parts)) >= P:
        print(i+1)
        break

if len(set(parts)) < P: print('paradox avoided')
    
    


##if len(set([input() for x in range(N)])) >= P:
##    print('yYAY')
##else: print('fk')
