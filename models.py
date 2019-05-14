STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA, PORAZ = 'W', 'X'

ABECEDA_VELIKE = 'ABCČDEFGHIJKLMNOPQRSŠTUVWXYZŽ'
ABECEDA_MALE = ABECEDA_VELIKE.lower()


class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        return list(set(self.crke) - set(self.geslo))

    def pravilne_crke(self):
        return list(set(self.crke) & set(self.geslo))
