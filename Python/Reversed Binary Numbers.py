def DecimalToBinary(num):
    return bin(num).replace("0b","")

y = str(DecimalToBinary(int(input())))

def BinaryToDecimal(num):
    return int(num,2)

z = BinaryToDecimal(y[::-1])
 
print(z)
        
