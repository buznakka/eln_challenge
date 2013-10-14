#!/usr/bin/python

import sys
import math

def get_n():
    if len(sys.argv) == 1:
        return 10
    else:
        return int(sys.argv[1])

def test_is_odd():
    return is_odd(1) and not is_odd(0)

def test_has_prime_factors():
    return has_prime_factors(100, [2,3,5,7]) and not has_prime_factors(7, [2,3,5])

def test_less_than_2():
    return less_than_2(1) and not less_than_2(2) and not less_than_2(3)

def test_has_brute_force_factors():
    return has_brute_force_factors(10) and not has_brute_force_factors(97)

def test_advance_trial():
    return advance_trial(2) == 3 and advance_trial(3) == 5

def test_get_primes():
    return get_primes(0) == [] and get_primes(1) == [2] and get_primes(2) == [2,3] and get_primes(10) == [2,3,5,7,11,13,17,19,23,29]
    
def tests_work():
    return test_less_than_2() and test_is_odd() and test_has_prime_factors() and test_has_brute_force_factors() and test_advance_trial() and test_get_primes()
    
def is_odd(num):
    return num % 2 == 1

def has_prime_factors(num, divisors):
    for divisor in divisors:
        if num % divisor == 0:
            return 1
    return 0

def less_than_2(num):
    return num < 2

def has_brute_force_factors(num):
    limit = int(math.sqrt(num))
    for divisor in range(2, limit + 1):
        if num % divisor == 0:
            return 1

    return 0

def advance_trial(num):
    if num < 3:
        return num+1
    else:
        return num+2

def get_primes(n):
    primes = []
    trial = 0
    while len(primes) < n:
        if not less_than_2(trial) and (is_odd(trial) or trial == 2) and not has_prime_factors(trial, primes) and not has_brute_force_factors(trial):
            primes.append(trial)

        trial = advance_trial(trial)
    
    return primes

def display_chart(primes):
    foo = '    '
    for x in primes:
        foo += '%(prime)4d' % {'prime': x}
    print(foo)
    
    foo = ''
    for x in primes:
        foo += '%(prime)4d' % {'prime': x}
        for y in primes:
            foo = foo + '%(product)4d' % {'product': x*y}
        print(foo)
        foo = ''

def main():
    if not tests_work():
        print("This code has issues. I'm sorry.")
        exit()
        
    primes = get_primes(get_n())
    display_chart(primes)

if __name__ == "__main__":
    main()
    
