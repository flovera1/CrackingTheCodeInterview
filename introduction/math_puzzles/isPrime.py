def isPrime(number):
    if number < 2:
        return False
    for i in range(2,number):
        if (number%i == 0):
            return False
    return True


def main():
    number = 4
    n      = isPrime(number)      
    print(n)

if __name__ == "__main__":
    main()