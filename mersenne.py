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
    
mps_found = 0
number = 2

print("Welcome to our Mersenne Prime finder script")
numberOfMPs = int(input("Please enter the number of Mersenne Primes to find:"))

while mps_found < numberOfMPs:
    mp = potential_MP(number)
    if(is_prime(mp)):
        mps_found += 1
        print(mp)
    number += 1
