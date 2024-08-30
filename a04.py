## IMPORTS GO HERE
## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####

def get_grade(grade):
    if grade == 90:
        return 'A+'
    elif grade >= 86:
        return 'A'
    elif grade >= 82:
        return 'A-'
    elif grade >= 78:
        return 'B+'
    elif grade >= 74:
        return 'B'
    elif grade >= 70:
        return 'B-'
    elif grade >= 66:
        return 'C+'
    elif grade >= 62:
        return 'C'
    elif grade >= 58:
        return 'C-'
    elif grade >= 54:
        return 'D+'
    elif grade >= 50:
        return 'D'
    else:
        return 'F'
    
def get_point(grade):
    if grade == 'A+':
        return 4.0
    elif grade == 'A':
        return 4.0
    elif grade == 'A-':
        return 3.7
    elif grade == 'B+':
        return 3.3
    elif grade == 'B':
        return 3.0
    elif grade == 'B-':
        return 2.7
    elif grade == 'C+':
        return 2.3
    elif grade == 'C':
        return 2.0
    elif grade == 'C-':
        return 1.7
    elif grade == 'D+':
        return 1.3
    elif grade == 'D':
        return 1.0
    else:
        return 0.0

#### End OF MARKER:

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
    
def calculate_sgpa(grade1, grade2, grade3):        
    total_points = get_point(grade1) + get_point(grade2) + get_point(grade3)
    sgpa = total_points / 3
    return sgpa
#### End OF MARKER:

get_grade(50)
calculate_sgpa('A+','A+','A+')
