def computeHCF(x, y):
    small = 0
    if(x < y ):
        small = x
    else:
        small = y

    hcf = 0  
    for i in range(1, small + 1 ):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

num1 = 12
num2 = 24
print("The HCF of 2 numbers {} and {} is {} ".format(num1 ,num2, computeHCF(num1, num2)))
