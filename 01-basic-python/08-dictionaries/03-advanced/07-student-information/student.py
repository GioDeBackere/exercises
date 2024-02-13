def process_data(string_data):
    students = {}
    for item in string_data:
        name, age, *courses = item.split(',')
        students[name] = {
            'age': int(age),
            'courses': courses
        }
    return students


def average_age(data):
    total_age = 0
    num_students = 0
    for student in data.values():
        total_age += student['age']
        num_students += 1
    return total_age / num_students
