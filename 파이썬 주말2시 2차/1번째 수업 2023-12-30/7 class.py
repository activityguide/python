# 클래스를 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean


class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

obj = MyClass(42)
obj.print_value()

students = [
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    student("운명월", 64, 88, 92, 92)
]

print("이름", "총점", '평균', sep="  ")
for student in students:
    print(student.to_string())