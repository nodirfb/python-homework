import json
# 1. Task: JSON Parsing
#     - write a Python script that reads the students.json JSON file and prints details of each student.

def student_parse():
    with open('students.json')as f:
        l = json.load(f)
    for student in l:
        print('name:', student['name'])
        print('age:', student['age'])
        print('grade:', student['grade'])
        print('subjects:', student['subjects'],end='\n\n')
student_parse()