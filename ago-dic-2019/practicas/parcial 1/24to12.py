def transform(time = None):
    #Obtener entrada si no se proporciona
    if time is None:
        time = raw_input("> ")

    #Deconstruir variables
    timelist = time.split(":")

    hours = int(timelist[0])
    minutes = timelist[1][0:2]
    subfix = timelist[1][2:]

    #am
    if hours < 12:
        if hours is 0:
            hours = 12
        subfix = "a.m."
    #pm
    else:
        subfix = "p.m."
        if hours is 12:
            hours = 12
        else:
            hours = hours % 12

    #Arreglar hrs a 2 digitos
    hours = str(hours)
    if len(hours) is 1:
        hours = "0" + hours


    return hours + ":" + minutes + subfix
