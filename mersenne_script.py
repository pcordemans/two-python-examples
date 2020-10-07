from mersenne import potential_MP, is_prime

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
