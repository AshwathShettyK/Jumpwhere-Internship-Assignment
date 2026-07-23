# Q12: Sort a list of tuples using lambda based on the second element.

subjects = [
    ('English', 88),
    ('Science', 90),
    ('Maths', 97),
    ('Social sciences', 82)
]

sorted_subjects = sorted(subjects, key=lambda item: item[1])
print("Sorted list based on marks:")
print(sorted_subjects)
