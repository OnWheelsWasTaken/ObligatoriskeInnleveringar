

verdi = float(input("Kor mykje pengar har du: "))
fraa = float(input("I frå kva år? "))
til = float(input("Til kva år? "))


def renteOkning(verdi, fraa, til):

    aar = til - fraa

    endring = verdi * (1.02 ** aar)

    return endring


print(round(renteOkning(verdi, fraa, til), 2), "NOK")
