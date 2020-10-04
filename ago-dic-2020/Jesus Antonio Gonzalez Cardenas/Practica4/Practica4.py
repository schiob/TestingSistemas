import csv
def getonedom(mail:str):
    x = mail.partition('@')
    dom = x[2]
    return dom.lower()


def getDomains(fpath):
    listdom = []
    with open(fpath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            temph = getonedom(row[1])
            vool = temph in listdom
            if vool == False:
                listdom.append(temph)
                 
    return listdom

def getAverages(fpath):
    countT  = 0
    results = dict()
    lisdom = getDomains(fpath)
    results = dict.fromkeys(lisdom,0)
    for i in lisdom:
        numl = []
        domstr = lisdom[countT]
        countT += 1
        with open(fpath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if getonedom(row[1]) == domstr:
                    numl.append(int(row[2]))
        actual_average = round(sum(numl)/(len(numl)),2)
        results[domstr] = actual_average


    return results
    

if __name__ == "__main__":
  print(getAverages('MOCK_DATA.csv'))
#   print(getAverages('Practica4TData.csv'))          

