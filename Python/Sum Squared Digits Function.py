for i in range(int(input())):
               p, b, K = map(int,input().split())
               ssd = 0
               while K:
                   ssd += (K % b) ** 2
                   K //= b
               print(p, ssd)
