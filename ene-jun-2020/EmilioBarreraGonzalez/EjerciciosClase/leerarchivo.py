def countChar(file_name):
    file = open(file_name, "r")
    count = 0
    content = file.read()

    for x in content:
        count+=1

    file.close()
    return count


if __name__ == "__main__":
    print(countChar("prueba.txt"))