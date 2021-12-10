class Ido:

    """A járművek elhaladásának ideje, az időértékek tárolása az osztályattribútumokban,
     és átváltása másodpercre a könnyebb számolás reményében..."""

    def __init__(self,ora:int,perc:int,masodperc:int):
        self.ora = ora
        self.perc = perc
        self.masodperc = masodperc
    def idomasodpercben(self):
        return self.ora * 3600 + self.perc * 60 +self.masodperc

    def __str__(self):
        ora = ""
        perc = ""
        masodperc = ""
        if(self.ora < 10):
            ora = "0" +str(self.ora)
        else:
            ora = str(self.ora)
        if (self.perc < 10):
            perc = "0" + str(self.perc)
        else:
            perc = str(self.perc)
        if (self.masodperc < 10):
            masodperc = "0" + str(self.masodperc)
        else:
            masodperc = str(self.masodperc)

        return ora+":"+perc+":"+masodperc