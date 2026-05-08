class JegyFoglalas:
    def __init__(self,utasnev,jarat,datum):
        self._utasnev = utasnev
        self._jarat = jarat
        self._datum = datum
    def get_utasnev(self):
        return self._utasnev
    def get_jarat(self):
        return self._jarat
    def get_datum(self):
        return self._datum

    def __str__(self):
        return (
            f"Utas: {self.utasnev},"
            f"Jaratszam: {self.jarat.get_utasnev()},"
            f"Celallomas: {self.jarat.get_celallomas()},"
            f"Datum: {self.datum},"
            f"Ar:{self.jarat.get_ar()} Ft"
        )

