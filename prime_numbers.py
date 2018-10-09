primes = [2, 3, 5, 7]
factors = []
#Challenge 1
#The Basics

def testingprimes(x):
    if x > 1:
        for i in range(2, 49):
            if x % i == 0:
                return False
            return True

        else:
            return False

print(testingprimes(332893298))

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
















