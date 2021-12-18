x = input()
y = int((len(x))/3)

words = [x[0:y],x[y:2*y],x[2*y:3*y]]
print(max(set(words),key = words.count))
