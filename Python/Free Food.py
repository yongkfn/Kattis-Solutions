food = []

for i in range(int(input())):
    a, b = map(int,input().split())
    food.append([i for i in range(a,b+1)])

print(len(set([day for sublist in food for day in sublist])))


## More readable
##flat_list = [day for sublist in food for day in sublist]
##print(len(set(flat_list)))

## OR JUST USE .extend()

