def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    total_grade = 0
    total_skipped = 0
    tests_completed = 0

    if grade1 is None:
        total_skipped += 1
    else:
        total_grade += grade1
        tests_completed += 1

    if grade2 is None:
        total_skipped += 1
    else:
        total_grade += grade2
        tests_completed += 1

    if grade3 is None:
        total_skipped += 1
    else:
        total_grade += grade3
        tests_completed += 1

    if grade4 is None:
        total_skipped += 1
    else:
        total_grade += grade4
        tests_completed += 1

    if grade5 is None:
        total_skipped += 1
    else:
        total_grade += grade5
        tests_completed += 1

    if total_skipped > 1 or (total_grade / tests_completed) < 12:
        return False
    else:
        return True


print(entrance_exam(12, 12, 12, 12, 12))
print(entrance_exam(12, 12, 12, None, 12))
print(entrance_exam(12, 12, 12, 2, 12))
print(entrance_exam(20, 20, 20, None, None))
