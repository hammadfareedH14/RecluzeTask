## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results):
  if results== None:
    return None
  cumulative_mark=[]
  for result in results:
    total_score = 0
    for scores in result[2:]:
      if scores!=None:
        total_score+=scores
    cumulative_mark.append((result[0],result[1],total_score))
  return cumulative_mark   

#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(results):
    cumulative_marks = find_cumulative_marks(results)
    top_students = []
    top_score = 0

    for student in cumulative_marks:
        if student[2] > top_score:
            top_score = student[2]
            top_students = [(student[0], student[1])]
        elif student[2] == top_score:
            top_students.append((student[0], student[1]))

    if len(top_students) == 1:
        return top_students[0]  
    else:
        return top_students  
   

#### End OF MARKER


if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
        
    ]

    print (find_cumulative_marks(results))
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print (find_top_student(results))
    # output: ('p101111', 'Ali Khayam')
