from safeexec import settimeout

#@settimeout(1)
def primes(maxPrimes):
    primes = []

    for i in range(2, maxPrimes):

        prime = True
        for prime in primes:
            if (i % prime == 0):
                prime = False
                break

        if (prime):
            primes.append(i)
            print ("Found prime: %s" % i)
