def factorsfind(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

num = int(input("Enter any number and I will list all the factors"))
print(f"The factors of {num} are: {factorsfind(num)}")

factorsfind(num)
