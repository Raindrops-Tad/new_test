import math
import decimal

def sqrt_binary(n):
    #n = decimal.Decimal(str(n))
    #temp = decimal.Decimal('0')
    temp = 0
    last = n
    floor = 0
    while True:
        if temp**2 > n:
            last = temp
        else:
            floor = temp
        temp = (floor+last)/2
        print("last = {}\ntemp = {}\ntemp^2 = {}\nfloor = {}".format(last,temp,temp**2,floor))
        if math.fabs(temp**2 - n) < 10**(-6):
            break
    return temp

num = float(input())
print(sqrt_binary(num))
print(math.e**(-6))
print(math.sqrt(num))
