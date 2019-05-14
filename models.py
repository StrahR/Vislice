import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA, PORAZ = 'W', 'X'


class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        return list(set(self.crke) - set(self.geslo))

    def pravilne_crke(self):
        return list(set(self.crke) & set(self.geslo))

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return len(self.pravilne_crke()) == len(set(self.geslo))

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        s = ['_']*len(self.geslo)
        pravilne_crke = self.pravilne_crke()
        for i, c in enumerate(self.geslo):
            if c in pravilne_crke:
                s[i] = c
        return ''.join(s)

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, c: str):
        if c in self.crke:
            return PONOVLJENA_CRKA
        self.crke.append(c)
        if c in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


bazen_besed = list()
with open("besede.txt", 'r') as fin:
    bazen_besed = fin.read().split('\n')
del bazen_besed[-1]
# print(besede[-1])


def nova_igra():
    return Igra(geslo=random.choice(bazen_besed), crke=[])
