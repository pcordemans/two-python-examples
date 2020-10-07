# Generates a potential Mersenne Prime
def potential_MP(n):
    return 2**n-1

# Returns True if number is a prime, if not False
def is_prime(number):
    if number <= 1:
        return False
    
    for divisor in range(2,number):
        if number % divisor == 0:
            return False

    return True    

# Returns True if number is the exponent of a Mersenne Prime
def is_mp(number):
    return is_prime(potential_MP(number))