import models


def izpis_igre(igra: models.Igra):
    return igra.pravilni_del_gesla() + '\nNepravilne črke:' + igra.nepravilni_ugibi()


def izpis_zmage(igra: models.Igra):
    return "BRAVO! Uganila si " + igra.geslo


def izpis_poraza(igra: models.Igra):
    return "PORAZ! Geslo je bilo " + igra.geslo


def zahtevaj_vnos():
    guess = input("Vnesi črko:\n> ").lower()
    while len(guess) > 1 and not guess.isalpha():
        guess = input("Vnesi črko:\n> ").lower()
    return guess


def pozeni_vmesnik():
    igra = models.nova_igra()
    while True:
        c = zahtevaj_vnos()
        status = igra.ugibaj(c)
        if status == models.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif status == models.PORAZ:
            print(izpis_poraza(igra))
            break
        else:
            print(izpis_igre(igra))


while True:
    pozeni_vmesnik()
    if input("Igraj znova (Y/n)").startswith('n'):
        break
