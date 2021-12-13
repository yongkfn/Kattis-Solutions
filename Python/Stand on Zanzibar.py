for j in range(int(input())):
    count = 0
    prev = 1
    booklet = list(map(int,input().split()))

    for i, number in enumerate(booklet):
        if (booklet[i]) > prev*2:
            count += (booklet[i]) - (prev * 2)
        prev = booklet[i]
    print(count)
