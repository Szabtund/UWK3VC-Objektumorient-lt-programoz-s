from abc import ABC

class Jarat(ABC):
    def __init__(self,jaratszam,celallomas,jegyar):
        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._jegyar = jegyar

    def get_jaratszam(self):
        return self._jaratszam
    def get_celallomas(self):
        return self._celallomas
    def get_jegyar(self):
        return self._jegyar

    def set_jegyar(self,ujar):
        if ujar > 0:
            self._jegyar = ujar
        else:
            raise ValueError("A jegyár nem lehet negatív!")

class Belfoldijarat(Jarat):
    def __init__(self,jaratszam,celallomas,jegyar):
        super().__init__(jaratszam,celallomas,jegyar)

class Nemzetkozijarat(Jarat):
    def __init__(self,jaratszam,celallomas,jegyar):
        super().__init__(jaratszam, celallomas, jegyar)
