x = str(input())
##print(x)

trik = [1, 0, 0]

for char in x:
##    print (char)
    if char == 'A':
        trik[0], trik[1] = trik[1], trik[0]
    elif char == 'B':
        trik[1], trik[2] = trik[2], trik[1]
    else: 
        trik[0], trik[2] = trik[2], trik[0]

for i, letter in enumerate(trik):
    if letter == 1:
        print(i+1)
