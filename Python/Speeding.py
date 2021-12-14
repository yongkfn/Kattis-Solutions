time = [0]
speed = [0]
max = 0

for i in range(int(input())):
               t, d = map(int,input().split())
               if t == 0 and d == 0:
                   continue
               time.append(t)
               speed.append(d)
##               print(time,speed)
               current_speed = (speed[i]-speed[i-1])/(time[i]-time[i-1])
##               print(current_speed)
               if current_speed > max:
                   max = int(current_speed)
                   
print(max)
                
