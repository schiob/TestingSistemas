def puntos(archivo):
    prom = []
    hotmail = {'puntos': [], 'dominio': 'hotmail.com'}
    gmail = {'puntos': [], 'dominio': 'gmail.com'}
    outlook = {'puntos': [], 'dominio': 'outlook.com'}
    
    
    with open(archivo) as File:
        reader = csv.DictReader(File)
        for i in reader:
            prom.append(i)

    for i in prom:
        if i['correo'].count('@hotmail.com'):
            hotmail['puntos'].append(int(i['puntos']))

        if i['correo'].count('@gmail.com'):
            gmail['puntos'].append(int(i['puntos']))

        if i['correo'].count('@outlook.com'):
            outlook['puntos'].append(int(i['puntos']))

    for i in range(0, len(hotmail['puntos'])):
        promediohotmail = 0.0
        promediohotmail += float(hotmail['puntos'][i])

    hotmail['promedio'] = promediohotmail/len(hotmail['puntos'])

    for i in range(0, len(gmail['puntos'])):

        promediogmail= 0.0
        promediogmail= float(gmail['puntos'][i])

    gmail['promedio'] = promediogmail/len(gmail['puntos'])

    for i in range(0, len(outlook['puntos'])):

        promesdiooutlook =0.0
        promesdiooutlook += float(outlook['puntos'][i])

    outlook['promedio'] = promesdiooutlook/len(outlook['puntos'])

    print(f'{hotmail["dominio"]} {hotmail["promedio"]}\n' f'{gmail["dominio"]} {gmail["promedio"]}\n' f'{outlook["dominio"]} {outlook["promedio"]}')


if __name__ == '__main__':
    main()