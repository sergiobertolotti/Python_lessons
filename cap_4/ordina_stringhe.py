def ordina(stringa):
    lis = list(stringa)
    lis.sort()
    for j in range(1,len(lis)):
        lis[0] += lis[j]
    return lis[0]

def fondi(stringa1, stringa2):
    stringa = ordina(stringa1 + stringa2)
    return stringa