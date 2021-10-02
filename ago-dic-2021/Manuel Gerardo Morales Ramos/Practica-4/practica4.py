def calc_prom() -> float:
    with open('archivito.txt', 'r') as file:
        total = count = 0
        
        for line in file:
            total += int(line)
            count += 1
        
        return 0 if count == 0 else total/count

if __name__ == "__main__":
    print(calc_prom())