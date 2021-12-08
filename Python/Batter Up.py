N = int(input())
numerator = 0

scores = map(int,input().split())
for score in scores:
    if score == -1:
        N -= 1
    else:
        numerator += score
print(numerator / N)
