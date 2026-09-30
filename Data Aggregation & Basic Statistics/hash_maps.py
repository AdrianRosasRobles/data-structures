def analyze_grades(grades):
    if not grades:
        return 0, 0
    
    total_grade = 0
    pass_count = 0
    num_students = len(grades)

    for student_id, grade in grades.items():
        total_grade += grade
        if grade >= 60:
            pass_count += 1
        
    average_grade = total_grade / num_students
    return average_grade, pass_count

student_grades = {
    "S101": 85,
    "S102": 55,
    "S103": 78,
    "S104": 92,
}

avg, passed = analyze_grades(student_grades)
print(f"Average Grade: {avg}")
print(f"Students who passed: {passed}")
