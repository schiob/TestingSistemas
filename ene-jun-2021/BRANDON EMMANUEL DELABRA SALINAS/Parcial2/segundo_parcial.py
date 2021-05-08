import os

def checkArchivoExiste(nombreArchivo:str)->str:
    archivo='./'+nombreArchivo

    if os.path.isfile(archivo):
        archivo_leer=open(nombreArchivo)
        lineas=archivo_leer.readlines()
        textofinal=''

        for linea in lineas:
            textofinal=textofinal+linea
        return textofinal

    else:
        return('El archivito no estaba pero mientras ve este bonito perrito:')
        print('                 ▄              ▄'
'                  ▌▒█           ▄▀▒▌'
'                  ▌▒▒█        ▄▀▒▒▒▐'
'                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐'
'               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐'
'             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌'
'            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌'
'            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐'
'           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌'
'           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌'
'          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐'
'          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌'
'          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐'
'           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌'
'           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐'
'            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌'
'              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀'
'                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀'
'                   ▒▒▒▒▒▒▒▒▒▒▀▀')


def convertirAMayusculas(textoConvertir:str):
    import requests

    url = "HTTP://API.SHOUTCLOUD.IO/V1/SHOUT"
    ntexto="{ \"INPUT\": \""+textoConvertir+"\"}"
    headers={'content-type': "application/json",}
    response = requests.request("POST", url, data=ntexto, headers=headers)

    return response.text

def funcionFinal(nombreDelArchivo:str):
    textoArchivo=checkArchivoExiste(nombreDelArchivo)
    ntexto=textoArchivo.replace('\n','')
    return convertirAMayusculas(ntexto)