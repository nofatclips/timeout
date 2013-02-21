from primes import primes
from fibo import fibonacci

if __name__ == '__main__':
    def workaround():
        from safeexec import settimeout
        global primes, fibonacci
        #import pickle
        #print (pickle.dumps(primes))
        primes = settimeout(1)(primes)
        fibonacci = settimeout(1)(fibonacci)

    workaround()
    primes(30000)
    fibonacci(30000)
    primes(25000)
