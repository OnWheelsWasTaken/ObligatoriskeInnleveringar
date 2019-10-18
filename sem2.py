#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import random


def oppgave1():
    """ Printer ut store tall i kort og lang form,
        ofte kalt amerikansk og britisk form.
    """
    store_tall = [
        ["Million", "10^6 ", "10^6 "],
        ["Milliard", "     ", "10^9 "],
        ["Billion", "10^9 ", "10^12"],
        ["Billiard", "     ", "10^15"],
        ["Trillion", "10^12", "10^18"],
        ["Quadrillion", "10^15", "10^24"],
        ["Quintillion", "10^18", "10^30"],
        ["Sextillion", "10^21", "10^36"]
    ]  # Hentet fra https://en.wikipedia.org/wiki/Names_of_large_numbers

    print("%-14s %8s %8s" % ("Navn", "Lang", "Kort"))
    for n in store_tall:
        print("%-15s %8s %8s" % (n[0], n[2], n[1]))


def oppgave2():
    """ Henter en rekke tall fra brukeren og ut hva som 
        var medianen i listen
    """
    liste123 = []

    print("Skriv inn so mange heiltal du vil, og avslutt med ferdig")
    avslSetning = "Medianen av verdiane er"
    while True:
        x = input()
        if x == 'ferdig':
            break
        liste123.append(int(x))
    liste123.sort()
    if len(liste123) % 2 == 0:
        op1 = int(len(liste123) / 2)
        op2 = op1 - 1
        median = (liste123[op1] + liste123[op2]) / 2
    else:
        median = liste123[int(len(liste123) / 2)]

    return avslSetning, median


# I billion USD (kort form)
microsoft_inntekt_dollar = [
    [2002, 28.37],
    [2003, 32.19],
    [2004, 36.84],
    [2005, 39.79],
    [2006, 44.28],
    [2007, 51.12],
    [2008, 60.42],
    [2009, 58.44],
    [2010, 62.48],
    [2011, 69.94],
    [2012, 73.12],
    [2013, 77.85],
    [2014, 86.83],
    [2015, 93.58],
    [2016, 85.32],
    [2017, 89.95],
    [2018, 110.36],
    [2019, 125.84]
]  # Hentet fra https://www.statista.com/statistics/267805/microsofts-global-revenue-since-2002/


def oppgave3a():
    """ Konverterer inntektene fra dollar til kroner
    uten å gjøre endringer på originallisten.
    """
    usdtilnok = 8.6862
    print("%-14s %-15s %-8s" % ("Aarstal", "USD", "NOK"))
    for n in microsoft_inntekt_dollar:
        print("%-15s %-15s %10s" % (n[0], n[1], (n[1] * usdtilnok)))


def oppgave3b():
    """ Tegner et histogram over inntektene til Microsoft
    """

    aar = []
    inntekt = []

    for i in range(len(microsoft_inntekt_dollar)):
        aar.append(microsoft_inntekt_dollar[i][0])
        inntekt.append(microsoft_inntekt_dollar[i][1])

    plt.bar(aar, inntekt)
    plt.show()


def oppgave3c():
    """ Summerer opp inntektene til Microsoft
    """
    summen = 0.0
    for x in range(len(microsoft_inntekt_dollar)):
        summen += microsoft_inntekt_dollar[x][1]
    print("Microsoft tjente", summen / 10 ** 3, "billioner dollar i perioden 2002-2019. ")


def print_kart(kart):
    """ Printer et 10 * 10 kart per rad
  input:
      kart, en list
  return:
      None"""
    for rad in kart:
        print("".join(rad))

    return None


def oppdater_kart(spelarX, spelarY, monsterX, monsterY):
    """ Printer et 10 * 10 kart med spiller i posisjon (spillerX, spillerY)
    og monster i posisjon (monsterX, monsterY)
    input:
        spillerX og spillerY, heltall mellom 0 og 9
    return:
        None
    """
    kart = []
    spelar = "   👮 "
    monster = "   👺 "
    bakgrunn = "   🌳 "
    for x in range(10):
        kart.append([])
        for y in range(10):
            if y == spelarY and x == spelarX:
                kart[x].append(spelar)
            elif y == monsterY and x == monsterX:
                kart[x].append(monster)
            else:
                kart[x].append(bakgrunn)

    # Printer kartet  ->
    print_kart(kart)


def flytt_spiller(bevegelse, spelarX, spelarY):
    """ Flytt spiller hvis lovlig trekk
    input:
        bevegelse: w,a,s,d
        spillerX og spillerY, heltall mellom 0 og 9
    return:
        spillerX, spillerY, heltall mellom 0 og 9
    """

    if bevegelse == 'w':
        if spelarX <= 0:
            pass
        else:
            spelarX -= 1
    elif bevegelse == 's':
        if spelarX >= 9:
            pass
        else:
            spelarX += 1
    elif bevegelse == 'a':
        if spelarY <= 0:
            pass
        else:
            spelarY -= 1
    elif bevegelse == 'd':
        if spelarY >= 9:
            pass
        else:
            spelarY += 1

    return spelarX, spelarY


def oppgave4():
    """ Spill mot monster"""
    """Definerer start-posisjon for spelar og monster"""
    spelarX = 1
    spelarY = 1

    monsterX = random.randint(0, 9)
    if monsterX <= 0 or monsterX >= 9:
        pass
    else:
        monsterX = random.randint(0, 9)
    monsterY = random.randint(0, 9)
    if monsterY <= 0 or monsterX >= 9:
        pass
    else:
        monsterY = random.randint(0, 9)

    """Lagar kartet med spelar og monster"""
    oppdater_kart(spelarX, spelarY, 3, 8)

    """Spel logikk"""
    vegardsspill = True
    total = 0

    while vegardsspill:
        print("Du må fanga fangen ved å prøva å ta han igjen \n"
              "pass på! Då han er veldig flink til å flytta seg")
        bevegelse = input('Flytt spiller ved å bruke \"wasd\": ')

        spelarX, spelarY = flytt_spiller(bevegelse, spelarX, spelarY)

        monster = 'wasd'
        bevegelse = random.choice(monster)

        monsterX, monsterY = flytt_spiller(bevegelse, monsterX, monsterY)

        oppdater_kart(spelarX, spelarY, monsterX, monsterY)
        # legg til trekk i total
        total += 1
        # If setning som avslutter spill dersom spiller er på monster x, y pos
        if spelarX == monsterX and spelarY == monsterY:
            print("Gratulera du har vunnet!", "\n"
                                              "Du klarte da på",
                  total, "trekk")
            vegardsspill = False


def main():
    """ Dette er filens main-funksjon, det er denne funksjonen som kjører
    når hele filen blir kjørt. 
    Hvis du vil kjøre en av oppgave-funksjonene nedenfor fjerner du #-tegnet 
    foran oppgave-funksjonen slik at den blir "skrudd på".
    Før du leverer kan det være lurt å sjekke alle funksjonene. Dette gjør 
    du ved å fjerne alle #-tegnene nedenfor.
    """
    oppgave1()
    # print()
    print(*oppgave2())
    # print()
    oppgave3a()
    oppgave3b()
    # print()
    oppgave3c()
    # print()
    oppgave4()
    # print()


main()
