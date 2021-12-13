for i in range (int(input())):
    count = 0
    booklet = list(map(int,input().split()))

    for i, number in enumerate(booklet):
        if booklet[i+1] == 0:
            break        
        count += (booklet[i+1]) - (int(number) * 2)

    if count >= 0:
        print(count)
    else: print(0)
