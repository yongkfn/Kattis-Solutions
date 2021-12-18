import math

x = int(input())

for i in range(1,99999999999,1):
    if x < math.ceil(1/6 *(2*i-1)*(2*i)*(2*i+1)):
        print(i-1)
        break
