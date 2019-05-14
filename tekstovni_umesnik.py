import models


def izris(n: int):
    if n == 0:
        return """\





      ────▀▀▀──
    """
    elif n == 1:
        return """\

       |
       |
       |
       |
      ─|──▀▀▀──
    """
    elif n == 2:
        return """\
       _____
       |
       |
       |
       |
      ─|──▀▀▀──
    """
    elif n == 3:
        return """\
       _____
       |   |
       |
       |
       |
      ─|──▀▀▀──
    """
    elif n == 4:
        return """\
       _____
       |   |
       |   o
       |
       |
      ─|──▀▀▀──
    """
    elif n == 5:
        return """\
       _____
       |   |
       |   o
       |   |
       |
      ─|──▀▀▀──
    """
    elif n == 6:
        return """\
       _____
       |   |
       |   o
       |  /|
       |
      ─|──▀▀▀──
    """
    elif n == 7:
        return """\
       _____
       |   |
       |   o
       |  /|\\
       |
      ─|──▀▀▀──
    """
    elif n == 8:
        return """\
       _____
       |   |
       |   o
       |  /|\\
       |  /
      ─|──▀▀▀──
    """
    elif n == 9:
        return """\
       _____
       |   |
       |   o
       |  /|\\
       |  /
      ─|──▀▀▀──
    """
    else:
        return """\
       _____
       |   |
       |   o
       |  /|\\
       |  / \\
      ─|──▀▀▀──
    """


def izpis_igre(igra: models.Igra):
    return izris(len(igra.napacne_crke())) + igra.pravilni_del_gesla() + '\nNepravilne črke:' + igra.nepravilni_ugibi()


def izpis_zmage(igra: models.Igra):
    return "BRAVO! Uganila si " + igra.geslo


def izpis_poraza(igra: models.Igra):
    return """\
       _____
       |   |
       |   |
       |   o
       |  /|\\
      ─|─┐/ \\┌─

    PORAZ!\nGeslo je bilo """ + igra.geslo + '.'


def zahtevaj_vnos():
    guess = input("Vnesi črko:\n> ").lower()
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Vnesi črko:\n> ").lower()
    return guess


def pozeni_vmesnik():
    igra = 1
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
