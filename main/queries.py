def get_students_and_there_courses_credits():
    return 'SELECT main_student.id, main_course.credits ' \
           'FROM main_student ' \
           'INNER JOIN main_course ON main_course.id=main_student.courses_id'


def get_teacher_disciplines_and_students_count():
    return 'SELECT *, count(mp.id) as count ' \
           'FROM main_course ' \
           'inner join main_professors mp on mp.id = main_course.professor_id ' \
           'inner join main_student ms on main_course.id = ms.courses_id ' \
           'group by mp.id'


def get_top_courses():
    return 'SELECT *, count(ms.courses_id) as count ' \
           'FROM main_course left join main_student ms on main_course.id = ms.courses_id ' \
           'group by main_course.id ' \
           'order by count desc'