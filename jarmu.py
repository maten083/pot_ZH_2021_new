from ido import Ido
class Jarmu:

    """A járművek bemérése ..."""

    def __init__(self,ido:Ido,rendszam:str):
        self.ido = ido
        self.rendszam = rendszam
        self.tipus = rendszam[0]
