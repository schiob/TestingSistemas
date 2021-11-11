from mocks import File
import re

# Primera parte
def get_students_average():
    students_file = File('students.txt').Read()
    students_list = students_file.split('\n')
    
    if not students_list:
        raise IndexError

    students_average = {}
    for i in range(len(students_list)):
        aux = students_list[i].split(' ')
        student_name = aux[0]
        score = aux[2]

        value = students_average.get(student_name)
        if value is None:
            students_average[student_name] = 0.0
        
        students_average[student_name] += float(score) 

    
    for key in students_average.keys():
        count = 0
        for student in students_list:
            match = re.search(r'{}\b'.format(key), student)
            if match:
                count += 1
        students_average[key] = students_average[key]/count

    return students_average

# Segunda parte
def add_student(data: str) -> bool:
    File('students.txt').Write(data)

def domain() -> bool:
    try:
        add_student(
            'Carla_Valdes probabilidad 70.00\nCarla_Valdes español 94.34\nCarla_Valdes geografia 85.00\nEstefanía_Gonzales calculo 85.00\nEstefanía_Gonzales fisica 76.50\nEstefanía_Gonzales quimica 89.49\nTomas_Ordaz programación 70.00\nTomas_Ordaz etica 97.60\nTomas_Ordaz redes 97.60\nJose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34'
        )
        get_students_average()
    except Exception:
        return False
    return True

def main():
    print(get_students_average())

if __name__ == '__main__':
    main()