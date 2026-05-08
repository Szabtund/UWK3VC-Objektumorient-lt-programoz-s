from abc import ABC

class Jarat(ABC):
    def __init__(self,jaratszam,celallomas,jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    def get_jaratszam(self):
        return self.jaratszam
    def get_celallomas(self):
        return self.celallomas
    def get_jegyar(self):
        return self.jegyar

    def set_jegyar(self,ujar):
        if ujar > 0:
            self.jegyar = ujar
        else:
            raise ValueError("A jegyár nem lehet negatív!")

class Belfoldijarat(Jarat):
    def __init__(self,jaratszam,celallomas,jegyar):
        super().__init__(jaratszam,celallomas,jegyar)

class Nemzetkozijarat(Jarat):
    def __init__(self,jaratszam,celallomas,jegyar):
        super().__init__(jaratszam, celallomas, jegyar)
