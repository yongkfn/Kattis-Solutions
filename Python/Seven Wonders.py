deck = str(input())
t = deck.count("T")
c = deck.count("C")
g = deck.count("G")
print(t,c,g)
seven = 0

numT = t/3
numC = c/3
numG = g/3
print(numT,numC,numG)

if numT <= numC and numT <= numG:
    seven = 7 * t
elif numC<=numT and numC<=numG:
    seven = 7 * c
elif numG<=numT and numG<=numC:
    seven = 7 * g
else: seven = 0

print ((t**2)+(c**2)+(g**2)+seven)

