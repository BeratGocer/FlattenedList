Liste = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]


def Duzenleme(Liste):
    DuzenlenmisListe = []

    for i in Liste:
        if isinstance(i, list):
            DuzenlenmisListe.extend(Duzenleme(i))
        else:
            DuzenlenmisListe.append(i)

    return DuzenlenmisListe


Cikti = Duzenleme(Liste)
print(Cikti)

Liste2 = [[1, 2], [3, 4], [5, 6, 7]]


def Duzenleme2(Liste2):
    DuzenlenmisListe2 = []

    for i in Liste2[::-1]:
        if isinstance(i, list):
            DuzenlenmisListe2.append(Duzenleme2(i))
        else:
            DuzenlenmisListe2.append(i)

    return DuzenlenmisListe2


Cikti2 = Duzenleme2(Liste2)
print(Cikti2)
