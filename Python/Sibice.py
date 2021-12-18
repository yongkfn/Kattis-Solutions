N, W, H = map(int,input().split())
[print('NE') if int(input()) > ((W**2 + H**2)**0.5) else print('DA') for i in range(N)]
