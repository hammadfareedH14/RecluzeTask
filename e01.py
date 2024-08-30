## IMPORTS GO HERE

## END OF IMPORTS


## START OF get_diag_sum FUNCTION
def get_diag_sum(n):
    if n % 2 == 0:  # Check if n is even
        return None
    
    # Initialize the sum to 1 (the center of the spiral)
    diag_sum = 1
    current_num = 1
    current_side_length = 1
    
    while current_side_length < n:
        # Increment side length
        current_side_length += 2
        
        # Add four corners of the current square to the diagonal sum
        for _ in range(4):
            current_num += current_side_length - 1
            diag_sum += current_num
    
    return diag_sum





if __name__ == '__main__':
    print(get_diag_sum(11))
