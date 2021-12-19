import functools

for i in range(int(input())):
    K, S = map(int,input().split())
    S1 = (functools.reduce(lambda a,b: a+b, [i for i in range(1,S+1,1)]))
    S2 = S * S
    S3 = S1 * 2
    print(K, S1, S2, S3)
