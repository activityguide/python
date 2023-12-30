# 학생 리스트를 선정, 딕셔너리 요소로 가진 리스트

students = [
    {'name': '유선우', 'korean': 91, 'math': 91, 'english': 91, 'science': 91},
    {'name': '사람1', 'korean': 92, 'math': 92, 'english': 92, 'science': 92},
    {'name': '유선웅', 'korean': 93, 'math': 93, 'english': 93, 'science': 93},
    {'name': '유선재', 'korean': 94, 'math': 94, 'english': 94, 'science': 94}
]
print("이름", "총점", '평균', sep="  ")
for student in students:
    score_sum = student['korean'] + student['math'] + student['english'] + student['science']
    score_average = score_sum / 4
    print(student['name'], score_sum, score_average, sep="  ")
