def grades_from_file(path):
    file = open(path)
    students = file.readlines()
    grades = []
    for i in students:
        x = i.replace('\n',' ')
        grades.append(x)
    students = grades    
    return students
    
def avg_from_file(data):
    grades = []
    for i in data:
        d = {'name': i[0], 'class': i[1], 'grade': i[2]}
        grades.append(d)

    Name = data[0].get('name')
    count = 0
    res = []
    for i in data:
        if Name == i.get('name'):
            count += float(i.get('grade'))
        else:
            avg = count/2
            res.append([Name, avg])
            count = 0
            Name = i.get('name')
    return res

if __name__ == '__main__':
    print (avg_from_file(grades_from_file("grade.txt")))