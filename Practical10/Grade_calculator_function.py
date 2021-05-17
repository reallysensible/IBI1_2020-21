def grade():
    name = input('Student name:')
    code = input('Student grade for the code portfolio:')
    poster = input('Student grade for the poster presentation:')
    exam = input('Student grade in the final exam:')
    total_grade = float(code)*0.4 + float(poster)*0.3 + float(exam)*0.3
    total_grade = ('%.3f' % total_grade)
    print(name, ':', 'final grade =', total_grade)

# example
grade()
student name
85
86
87
