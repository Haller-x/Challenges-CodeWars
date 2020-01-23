def namelist(names):
    y = len(names)
    voltar = ''
    if y == 0:
        return ''
    elif y == 1:
        return names[0]['name']
    elif y == 2:
        return names[0]['name'] + " & " + names[1]['name']

    elif (y > 2):
        for i in range(0, len(names) - 1):
            voltar = voltar + names[i]['name'] + ", "
        voltar = voltar[:-2] + " & " + names[y - 1]['name']
    return voltar
