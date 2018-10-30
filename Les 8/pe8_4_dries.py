studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    gemiddelde_lijst = []
    for student in studentencijfers:
        gemiddelde = sum(student)//len(student)
        gemiddelde_lijst.append(gemiddelde)
    return gemiddelde_lijst


def gemiddelde_van_alle_studenten(studentencijfers):
    return sum(gemiddelde_per_student(studentencijfers))//len(gemiddelde_per_student(studentencijfers))


print(gemiddelde_per_student(studentencijfers), end="\n\n")
print(gemiddelde_van_alle_studenten(studentencijfers))