m = int(input("Enter one number: "))
if m > 1:
    for i in range(2, int(m**0.5) + 1):  # Check divisors up to the square root of m
        if m % i == 0:
            print(f"{m} is not a prime number!")
            break
    else:
        print(f"{m} is a prime number!")
else:
    print(f"{m} is not a prime number!")
