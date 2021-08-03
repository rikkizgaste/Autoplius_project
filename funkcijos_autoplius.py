
def isvalyk(sarasas):
    sarasas1 = []
    for index, item in enumerate(sarasas):
        a = round(((index - 20) / 1.25) % 20, 2)
        if a == 0 or a == 0.8 or a == 1.6 or a == 2.4 or a == 3.2:
            continue
        else:
            sarasas1.append(item)
    return sarasas1


def sutvarkyk_kaina(sarasas):
    sarasas1 = []
    for a in sarasas:
        a = [i for i in a.split() if i != "€"]
        sarasas1.append(''.join(a))
    return sarasas1


def sutvarkyk_data(sarasas):
    sarasas1 = []
    for i in sarasas:
        if len(i) > 4:
            b = i.split("-")
            sarasas1.append(b[0])
        else:
            sarasas1.append(i)
    return sarasas1


c = ["3 000 000 €", "4 000 000 €"]
# c = sutvarkyk_kaina(c)
d = ["2009-03", "2012", "2003-06", "2015"]
# d = sutvarkyk_data(d)
# print(d)
