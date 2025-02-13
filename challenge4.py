def greatcomfac(num1,num2):
    smaller = min(num1,num2)
    gcf = 1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i ==0:
            gcf = i
    return gcf

num1 = int(input("Enter any number"))
num2 = int(input("Enter another number"))
print(f"The greatest common factor of {num1} and {num2} is {greatcomfac(num1, num2)}")
