def get_students_and_there_courses_credits():
    return 'SELECT main_student.id, main_course.credits ' \
           'FROM main_student ' \
           'INNER JOIN main_course ON main_course.id=main_student.courses_id'
