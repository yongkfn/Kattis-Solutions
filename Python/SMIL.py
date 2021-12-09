x = list(input())

for i, letter in enumerate(x):
##    print(i,letter)
    if letter == ':' or letter == ';':
        try:
            if x[i+1] == ')':
                print(i)
            elif x[i+1] == '-' and x[i+2] == ')':
                print(i)
        except:
            continue
