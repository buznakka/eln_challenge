#!/usr/bin/python

import sys
import math

def get_n():
    if len(sys.argv) == 1:
        return 10
    else:
        return int(sys.argv[1])

def test_is_even():
    return is_even(0) and not is_even(1)

def test_has_prime_factors():
    return has_prime_factors(100, [2,3,5,7]) and not has_prime_factors(7, [2,3,5])

def test_less_than_2():
    return less_than_2(1) and not less_than_2(2) and not less_than_2(3)

def test_has_brute_force_factors():
    return has_brute_force_factors(24, [2,3]) and not has_brute_force_factors(97, [2,3,5,7])

def test_advance_trial():
    return advance_trial(2) == 3 and advance_trial(3) == 5

def test_get_primes():
    return get_primes(0) == [] and get_primes(1) == [2] and get_primes(2) == [2,3] and get_primes(10) == [2,3,5,7,11,13,17,19,23,29]
    
def tests_work():
    return test_less_than_2() and test_is_even() and test_has_prime_factors() and test_has_brute_force_factors() and test_advance_trial() and test_get_primes()
    
def is_even(num):
    return num % 2 == 0

def has_prime_factors(num, divisors):
    for divisor in divisors:
        if num % divisor == 0:
            return 1
    return 0

def less_than_2(num):
    return num < 2

def has_brute_force_factors(num, primes):
    limit = int(math.sqrt(num))
    for divisor in range(2, limit + 1):
        if divisor in primes:
            continue
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
        if less_than_2(trial):
            pass
        elif is_even(trial) and trial != 2:
            pass
        elif has_prime_factors(trial, primes):
            pass
        elif has_brute_force_factors(trial, primes):
            pass
        else:
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
    
