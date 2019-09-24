# coding=utf-8
# Semesteroppgove Vegard Berge

# oppgove 1


tall_1 = int(input("Tall nr 1: "))
tall_2 = int(input("Tall nr 2: "))
tall_3 = int(input("Tall nr 3: "))
print("Dine tall var: \n",  "Tall nr 1: " + str(tall_1), "\n Tall nr 2: " + str(tall_2), "\n Tall nr 3: " + str(tall_3))


if tall_1 < tall_2 < tall_3:
    print("Disse tallene er stigende. ")

elif tall_1 > tall_2 > tall_3:
    print("Disse tallene er synkande. ")

else:
    print("Disse tallene står ikkje i ei rekkefylgje. ")

# oppgave 2a

x = input("Skriv inn din sort: (D, H, S, C): ").upper()

if x == 'D':
    print("Ruter")
elif x == 'H':
    print("Hjerter")
elif x == 'S':
    print("Spar")
elif x == 'C':
    print("Klover")


# oppgåve 2b
Kortstokk = {'K': 'Konge', 'Q': 'Dronning', 'J': 'Knekt', '1': 'Ein', '2': 'To', '3': 'Tre', '4': 'Fira', '5': 'Fem',
             '6': 'Seks',
             '7': 'sju', '8': 'aatta', '9': 'Ni', '10': 'Ti', 'A': 'Ess'}
x = input("Eit kort frå kortstokken takk: ").upper()
print(Kortstokk[x])

# Bonus! Her har eg kombinert oppgåve 2a og 2b i ein kode som eg syntes var betre.
# Ignorer denne dersom dykkar ikkje tell denne med.


kort = input("Skriv inn da kortet du vil at maskina skal tyde (døme 4C = Kløver fira): ").upper()
liste = list(kort)


def dinkorttype(typen):
    farge = {
        "D": "Ruter",
        "H": "Hjerter",
        "S": "Spar",
        "C": "Kløver"
    }
    verdiane = {
        "A": "Ess",
        "2": "To",
        "3": "Tre",
        "4": "Fira",
        "5": "Fem",
        "6": "Seks",
        "7": "Sju",
        "8": "Åtte",
        "9": "Ni",
        "10": "Ti",
        "J": "Knekt",
        "Q": "Dame",
        "K": "Konge"
    }
    # Returnerar riktig verdi basert på brukar-input
    return farge[typen[1]] + " " + verdiane[typen[0]]


print(dinkorttype(liste))


# oppgave3.a
kursen = {
    "EUR": 9.68551,
    "USD": 8.50373,
    "GBP": 11.0950,
    "AUD": 6.06501,
    "SEK": 0.92950,
    "NOK": 1.00000
}

beløp = float(input("Beløp: "))
valuta = input("Valutta: ").upper()

print(round((beløp * kursen[valuta]), 2), "NOK")

# 3.b
# Nyttar same dictonary frå 3.a

beløp_2 = float(input("Beløp: "))
valuta = input("Valutta: ").upper()

print(round((beløp_2 / kursen[valuta]), 2), valuta)

print()

# Oppgave4

for n in range(0, 11):
    print(str(n) + "**" + str("3"), str("="), str(n ** 3))

# Oppgave5a

start = int(input("Start: "))
stopp = int(input("Stop: "))
vilkaar = int(input("Delelig på: "))

print("Start: ", str(start))
print("Stop: ", str(stopp))
print("n: ", str(stopp))
print("Verdiar mellom", str(start), "og", str(stopp), "som er delelige på", str(vilkaar))

for n in range(start, stopp + 1):
    if n % vilkaar == 0:
        print(n)


# Oppgave6a


def tilfahrenheit(celsius):
    return int(celsius * 1.800) + 32


print("Celsius     Fahrenheit")
for n in range(0, 101, 10):
    print("%8d %10d " % (n, tilfahrenheit(n)))


# Oppgåve 6b

def tilfahrenheit(celsius):
    return int(celsius * 1.800) + 32


print("Celsius      Fahrenheit     Status")
for n in range(0, 101, 10):
    if n <= 60:
        print("%8d %10d %15s" % (n, tilfahrenheit(n), str("Eg har det bra.")))
    else:
        print("%8d %10d %15s" % (n, tilfahrenheit(n), str("Eg har det bra.")))

print()
print()

#oppgave 7

verdi = float(input("Kor mykje pengar har du: "))
fraa = float(input("I frå kva år? "))
til = float(input("Til kva år? "))


def renteOkning(verdi, fraa, til):

    aar = til - fraa

    endring = verdi * (1.02 ** aar)

    return endring


print(round(renteOkning(verdi, fraa, til), 2), "NOK")
