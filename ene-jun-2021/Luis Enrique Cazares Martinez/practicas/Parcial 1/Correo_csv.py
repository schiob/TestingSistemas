import csv


def puntos(archivo):
    results = []
    hotmail = {'puntos': [], 'dominio': 'hotmail.com'}
    gmail = {'puntos': [], 'dominio': 'gmail.com'}
    outlook = {'puntos': [], 'dominio': 'outlook.com'}
    sh = 0.0
    sg = 0.0
    so = 0.0
    with open(archivo) as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)

    for i in results:
        if i['correo'].count('@hotmail.com'):
            hotmail['puntos'].append(int(i['puntos']))

        if i['correo'].count('@gmail.com'):
            gmail['puntos'].append(int(i['puntos']))

        if i['correo'].count('@outlook.com'):
            outlook['puntos'].append(int(i['puntos']))

    for i in range(0, len(hotmail['puntos'])):
        sh += float(hotmail['puntos'][i])

    hotmail['promedio'] = sh/len(hotmail['puntos'])

    for i in range(0, len(gmail['puntos'])):
        sg += float(gmail['puntos'][i])

    gmail['promedio'] = sh/len(gmail['puntos'])

    for i in range(0, len(outlook['puntos'])):
        so += float(outlook['puntos'][i])

    outlook['promedio'] = so/len(outlook['puntos'])

    print(f'{hotmail["dominio"]} {hotmail["promedio"]}\n'
          f'{gmail["dominio"]} {gmail["promedio"]}\n'
          f'{outlook["dominio"]} {outlook["promedio"]}')


def main():
    puntos('correos.csv')


if __name__ == '__main__':
    main()
