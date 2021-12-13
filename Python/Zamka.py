min = int(input())
max = int(input())
X = int(input())

def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

for i in range(min,max+1,1):
    if sum_digits(i) == X:
        print(i)
        break

for j in range(max,min-1,-1):
    if sum_digits(j) == X:
        print(j)
        break
