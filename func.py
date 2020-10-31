import random, csv

class students:
    def __init__(self, before="", after=""):

        students_file = csv.reader(open('students.csv', 'r'))
        
        student_row = sum([i for i in students_file],[])

        random_student = random.choice(student_row)

        print (f"{before}{random_student}{after}")
    
    def all():

        students_file = csv.reader(open('students.csv', 'r'))
        
        student_row = sum([i for i in students_file],[])

        print (student_row)

    #returns one random student per line for the number of lines specified in the "count" parameter
    def random_limited(count=1):
        
        students_file = csv.reader(open('students.csv', 'r'))
        
        student_row = sum([i for i in students_file],[])

        i = 0

        while (i < count):
            random_student = random.choice(student_row)
            print (f"{random_student}")
            i += 1

    #returns the students in alphabetical order
    def alphabetize():

        students_file = csv.reader(open('students.csv', 'r'))

        student_row = sum([i for i in students_file],[])
        student_row.sort()
        for student in student_row:
            print(student)
        

            



