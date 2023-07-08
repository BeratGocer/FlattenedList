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