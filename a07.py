grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
def calculate_sgpa(grades):

    if grades == None:
        return None

    if not isinstance(grades, list):
        grades = [grades]

     
    len_list = len(grades)

    # handle zero division errors.
    if len_list == 0:
        return False
    
    gpa = 0.0    

    for result in grades:
        
        if result=='A+':
            gpa += 4.00
        elif result == 'A':
            gpa += 4.00
        elif result== 'A-':
            gpa += 3.67
        elif result == "B+":
            gpa += 3.33
        elif result == 'B':
            gpa += 3.00
        elif result == 'B-':
            gpa += 2.67
        elif result == 'C+':
            gpa += 2.33
        elif result == 'C':
            gpa += 2.00
        elif result == 'C-':
            gpa += 1.67
        elif result == 'D+':
            gpa += 1.33
        elif result == 'D':
            gpa += 1.00
        else:
            return None

    sgpa = gpa /len_list
    return sgpa       
#### End OF MARKER
### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
credit_hours = [4.0,4.0,4.0,3.0,3.0,3.0,2.0,2.0,2.0,1.0,1.0]
def calculate_sgpa_weighted(grades, credit_hours):
    
    if not isinstance(grades, list):
        grades = [grades]

    if not isinstance(credit_hours, list):
        credit_hours = [credit_hours]

    
    if len(grades) != len(credit_hours):
        return None
    
    gpa_point = []
    
    total_credits_point = sum(credit_hours)

    for grade in grades:

        if grade == "A+":
            gpa_point.append(4.00)
        elif grade == "A":
            gpa_point.append(4.00)
        elif grade == "A-":
            gpa_point.append(3.67)
        elif grade == "B+":
            gpa_point.append(3.33)
        elif grade == "B":
            gpa_point.append(3.00)
        elif grade == "B-":
            gpa_point.append(2.67)
        elif grade == "C+":
            gpa_point.append(2.33)
        elif grade == "C":
            gpa_point.append(2.00)
        elif grade == "C-":
            gpa_point.append(1.67)
        elif grade == "D+":
            gpa_point.append(1.33)
        elif grade == "D":
            gpa_point.append(1.00)
        elif grade == "F":
            gpa_point.append(0.0)
        else:
            return None  
    total_gpa_points = 0
    # gpa_point list and credit hours list is multiplying together to get total gpa = ---->>>   
    for i in range(len(gpa_point)):
        total_gpa_points =total_gpa_points + gpa_point[i] * credit_hours[i]
    
    sgpa = total_gpa_points / total_credits_point
    return sgpa  

### End OF MARKER
print(calculate_sgpa(['A+',"B+","C-"]))
print(calculate_sgpa_weighted(["A+"],[4]))