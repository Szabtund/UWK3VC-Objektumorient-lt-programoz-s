from foglalas import JegyFoglalas

class LegiTarsasag:
    def __init__(self,nev) :
        self._nev = nev
        self._jaratok = []
        self._foglalasok = []

    def jarat_hozzaadas(self,jarat):
        self._jaratok.append(jarat)
    def foglalas(self,utasnev,jaratszam,datum):
        for jarat in self._jaratok:
            if jarat.get_jaratszam()==jaratszam:
                ujfoglalas = JegyFoglalas(utasnev,jarat,datum)
                self._foglalasok.append(ujfoglalas)
                return f"Sikeres foglalas! Ar: {jarat.get_jegyar()} Ft"
        raise ValueError("Nincs ilyen jarat")
    def foglalas_lemondasa(self,utasnev,jaratszam):
        for foglalas in self._foglalasok:
            if (
                foglalas.get_utasnev()==utasnev
                and foglalas.get_jarat().get_jaratszam()==jaratszam
            ):
                self._foglalasok.remove(foglalas)
                return "Foglalas sikeresen torolve."
        raise ValueError("A foglalas nem talalhato!")
    def foglalasok_listazasa(self):
        if not self._foglalasok:
            print ("Nincsenek foglalasok.")
            return
        for foglalas in self._foglalasok:
            print(foglalas)


