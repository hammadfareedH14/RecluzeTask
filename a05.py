## IMPORTS GO HERE
## END OF IMPORTS
#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(n):

    if not isinstance(n, int) :
        return False  
    if n <= 1:
        return False 

    for i in range(2, int(n/2)+ 1):
        if n % i == 0:
            return False 
    return True
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(number=15):
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(number):
     
    if number <= 1:
        return None  
    for i in range(int(number), 2, -1): 
        if is_prime(i):
            return i

    return None 
#### End OF MARKER

is_prime(499) 
get_largest_prime(10)
output_factors(10)  
