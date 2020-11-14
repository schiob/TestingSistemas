import csv

def validate_file(fpath:str):
    anythn = ""
    with open(fpath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ' ')
        for row in csv_reader:
            anythn = anythn+str(row)+"\n" 

    if anythn != "":
        return True
    else:
        return False       

def read_alumn_data(fpath:str):
    data_list = []
    with open(fpath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        for row in csv_reader:
            data_list.append(row)
    return data_list

def get_names(data_list:list):
    names = []
    for y in range(len(data_list)):
        if y == 0:
            actual = data_list[y]
            names.append(actual[0])
        else:
            actual_data = data_list[y][0]
            last_data = data_list[y-1][0]
            if last_data != actual_data:
                names.append(actual_data)
    return names

def get_averages(data:list):
    names = get_names(data)
    results = dict.fromkeys(names,0)
    califs = []
    for i in range(len(names)):
        actual_name = names[i]
        for x in range(len(data)):
            if actual_name == data[x][0]:
                califs.append(float(data[x][2]))
        average = round(sum(califs)/len(califs),2)
        califs.clear()
        results[names[i]] = average

    return results

if __name__ == "__main__":
    lis = read_alumn_data("promedios3.csv")
    names = get_names(lis)
    print(lis)
    print(names)
    print(get_averages(lis))