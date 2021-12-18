import math

opposite, angle = map(int,input().split())
print(math.ceil(opposite / math.sin(math.radians(angle))))
