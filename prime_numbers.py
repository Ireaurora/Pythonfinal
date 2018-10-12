primes = [2, 3, 5, 7]

factors = []
#Challenge 1
#The Basics

num = int(input("What number would you like to test?"))
def testing_prime_number(num):
    if num > 1:
        # checking for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number because it's less than 1 and prime numbers are greater than one")


#The advanced bit
def testingmoreprimes(x):
    if x > 1:
        for i in primes:
            if x % i == 0:
                return False
            return True

        else:
            return False

print(testingmoreprimes(34343))

#The clever one

def savingprimes(x):
    if x > 1:
        for i in primes:
            if x % i == 0:
                return False
            return newlist(x)
        else:
            return False

def newlist(x):
    primes.append(x)
    return primes

print(savingprimes(3298091803288838238291))

#The olympian challenge

def getfactors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

print(getfactors(320))

def savingprimes(x):
    if x > 1:
        for i in primes:
            if x % i == 0:
                return False
            return primeslist(x)
        else:
            return False

def primeslist(x):
    factors.add(x)
    return factors













