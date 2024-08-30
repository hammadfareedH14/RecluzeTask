## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x, guess=1.1): 
    if x < 0: 
        return None 
    
    if good_enough(guess, x): 
        return guess 
    
    else: 
        new_guess = improve_guess(guess, x)  
        return sqrt(x, new_guess)
    
def good_enough(guess, x): 
    if abs(guess * guess - x) < 0.1: 
        return True
    else: 
        return False

    
#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(a, b):
    return (a + b) / 2.0

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess, x):
    x=x*1.0
    return average(guess, x / guess)

#### End OF MARKE

v=sqrt(16,3.8)
#### End OF MARKER
