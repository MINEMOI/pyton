number = int(input("dime el numero del cual quieres la tabla"))
number_to_m = 11

while number_to_m != 0:
    number_to_m -= 1
    result = number * number_to_m
    print (f"{number} x {number_to_m} = {result}")
