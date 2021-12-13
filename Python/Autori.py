import sys
x = sys.stdin.readline().strip()
print(''.join([y for y in x if y.isupper()]))


##x = input().split('-')
##y = ''
##
##for i in range(len(x)):
##    y += x[i][0]
##
##print(y.strip())
