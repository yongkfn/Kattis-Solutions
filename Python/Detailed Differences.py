for i in range(int(input())):
    A, B = input(), input()
    print(A)
    print(B)
    print(''.join(['.' if A[i] == B[i] else '*' for i in range(len(A))]),'\n')
