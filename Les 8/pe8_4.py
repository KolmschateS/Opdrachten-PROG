notes = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]
len_notes = len(notes)


def average_per_student():
    average_list = []
    for student in notes:
        average = sum(student) / len(student)
        average_list.append(average)
    return average_list


def average_all_students():
    average_all = sum(average_per_student()) // len(average_per_student())
    return int(average_all)


print(average_per_student())
print(average_all_students())