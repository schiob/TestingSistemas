"""de 2:23pm
a 14:23"""
def horario(s):
    i = 0
    hrs =[]
    if s[5] == 'a' and int(s[3]) < 6:
        while i < len(s):
            if  s[i] != '.' and s[i]!='a' and s[i]!='m':
                hrs.append(s[i])
            i+=1
        r = print(''.join(hrs)+'hrs')

    elif s[5] == 'p' and int(s[3]) < 6:
        while i < len(s):
            if i == 3 or i == 4:
                hrs.append(s[i])

            if  s[i] != '.' and s[i]!='p' and s[i]!='m' and len(hrs) < 3 :
                if s[i] == ':':
                    hrs.append(s[i])
                if len(hrs) < 1:
                    if s[0] == '0' and s[1] == '1':
                        hrs.append('13')
                    elif s[0] == '0' and s[1] == '2':
                        hrs.append('14')
                    elif s[0] == '0' and s[1] == '3':
                        hrs.append('15')
                    elif s[0] == '0' and s[1] == '4':
                        hrs.append('16')
                    elif s[0] == '0' and s[1] == '5':
                        hrs.append('17')
                    elif s[0] == '0' and s[1] == '6':
                        hrs.append('18')
                    elif s[0] == '0' and s[1] == '7':
                        hrs.append('19')
                    elif s[0] == '0' and s[1] == '8':
                        hrs.append('20')
                    elif s[0] == '0' and s[1] == '9':
                        hrs.append('21')
                    elif s[0] == '1' and s[1] == '0':
                        hrs.append('22')
                    elif s[0] == '1' and s[1] == '1':
                        hrs.append('23')
                    elif s[0] == '1' and s[1] == '2':
                        hrs.append('00')
            i+=1
        r = print(''.join(hrs)+'hrs')
    return r

if __name__ == '__main__':
    hrs = []
    s = str(input())
    horario(s)
