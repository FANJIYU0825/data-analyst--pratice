import json
from src.util import ddb_util, py_util


if __name__ == '__main__':
    group_school = 'Studycat::School of Jake'
    teacher_code = 'ZJBELR'
    class_code = 'QBDRPE'

    ddb = ddb_util.LambdaDDB(profile_name='cnprod')

    teacher = ddb.query_one(
        table_name='teachers',
        condition='#gs = :gs and username = :un',
        attr_names={'#gs': 'group::school'},
        attr_values={':gs': {'S': group_school},
                     ':un': {'S': teacher_code}}
    )

    teacher_user_account = ddb.query_one(
        table_name='user-accounts',
        condition='username = :un',
        attr_values={':un': {'S': teacher_code}},
        error_not_found=True)

    _class = ddb.query_one(
        table_name='classes',
        condition='username = :un and code = :cc',
        attr_values={':un': {'S': teacher_code},
                     ':cc': {'S': class_code}})

    student_assignments = ddb.query(
        table_name='student-assignments',
        condition='class_code = :cc',
        attr_values={':cc': {'S': _class['code']}})

    students = ddb.query(
        table_name='students',
        condition='class_code = :cc',
        attr_values={':cc': {'S': class_code}})

    student_user_accounts = []
    student_experience = []
    for student in students:
        student_user_account = ddb.query_one(
            table_name='user-accounts',
            condition='username = :un',
            attr_values={':un': {'S': student['student_pin']}},
            error_not_found=True)
        student_user_accounts.append(student_user_account)

        student_experience += ddb.query(
            table_name='experience',
            index_name='usr-date-index',
            condition='usr = :usr',
            attr_values={':usr': {'S': student['student_pin']}})

    data = {
        'teachers': [teacher],
        'classes': [_class],
        'students': students,
        'student-assignments': student_assignments,
        'experience': student_experience,
        'user-accounts': [teacher_user_account] + student_user_accounts}

    data = json.dumps(data, cls=py_util.DecimalEncoder)
    file_name = 'src/functions/create_demo_teacher/jakes_data_20190418.json'
    with open(file_name, 'w') as f:
        f.write(data)
