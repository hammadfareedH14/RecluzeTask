## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def output_prime_factors(n):
    n = round(n) 
    for i in range(n+1):
        if is_prime(i) and n%i==0: 
            print(i)
       

#### End OF MARKER

### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(n):
    if not isinstance(n, int) or n <= 0:
        return None
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 1
#### End OF MARKER


output_prime_factors(23)
print(get_nth_prime(4))
