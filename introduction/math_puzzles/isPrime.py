def isPrime(number):
    if number < 2:
        return False
    for i in number:
        if (i%2 == 0):
            return False
    return True


        