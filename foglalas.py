class JegyFoglalas:
    def __init__(self,utasnev,jarat,datum):
        self.utasnev = utasnev
        self.jarat = jarat
        self.datum = datum
    def get_utasnev(self):
        return self.utasnev
    def get_jarat(self):
        return self.jarat
    def get_datum(self):
        return self.datum

    def __str__(self):
        return (
            f"Utas: {self.utasnev},"
            f"Jaratszam: {self.jarat.get_utasnev()},"
            f"Celallomas: {self.jarat.get_celallomas()},"
            f"Datum: {self.datum},"
            f"Ar:{self.jarat.get_ar()} Ft"
        )

