# 딕셔너리를 리턴하는 함수를 선언, 반복되는 키 입력을 출입

def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

students = [
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("운명월", 64, 88, 92, 92)
]

# 학생을 처리하는 함수를 선언
def student_get_sum(student):
    return student['korean'] + student['math'] + student['english'] + student['science']


def student_get_average(student):  # 평균 구함
    return student_get_sum(student) / 4

def student_to_string(student):
    return print(f'{student["name"], student_get_sum(student), student_get_average(student)}')

print("이름", "총점", '평균', sep="  ")
for student in students:
    student_to_string(student)

