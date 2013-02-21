from safeexec import settimeout

#@settimeout(1)
def fibonacci(maxFibo):
    fibo, prec = 1,0
    while (fibo<=maxFibo):
        print (fibo)
        fibo, prec = fibo + prec, fibo
