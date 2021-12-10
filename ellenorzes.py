from jarmu import Jarmu
from ido import Ido

class Ellenorzes:
    def __init__(self):
        self.jarmuvek = []
    def beolvas(self)->None:
        print("1. feladat: A jarmu.txt beolvasása.")
        try:
            f = open("jarmu.txt", "r", encoding="UTF-8")
            for sor in f:
                sortomb= sor.strip().split()
                ido = Ido(int(sortomb[0]),int(sortomb[1]),int(sortomb[2]))
                jarmu = Jarmu(ido, sortomb[3])
                self.jarmuvek.append(jarmu)
            f.close()
        except FileNotFoundError:
            print("hiba a fájl beolvasásakor")
    def feladat2(self):
        start=self.jarmuvek[0].ido.ora
        veg = self.jarmuvek[len(self.jarmuvek) - 1].ido.ora
        munkaido = veg-start
        print("2. feladat: Az ellenőrzést végzők legalább ",munkaido," órát dolgoztak.")
    def feladat3(self):
        buszdb = 0
        kamiondb = 0
        motordb = 0
        kocsidb = 0
        for jarmu in self.jarmuvek:
            if jarmu.tipus == "B" :
                buszdb+=1
            elif jarmu.tipus == "K":
                kamiondb += 1
            elif jarmu.tipus == "M":
                motordb += 1
            else:
                kocsidb += 1
        print("3. feladat: Elhaladt járművek mennyisége típusonként:")
        print("\tautóbusz: ",buszdb)
        print("\tkamion: ",kamiondb)
        print("\tmotor: ",motordb)
        print("\tszemelygépkocsi: ",kocsidb)

    def feladat4(self):
        maxidokulonbseg = -1
        kezdoido = Ido(0,0,0)
        vegido = Ido(0, 0, 0)
        for i in range(0,len(self.jarmuvek)-2):
            if ((self).jarmuvek[i+1].ido.idomasodpercben() - self.jarmuvek[i].ido.idomasodpercben()) > maxidokulonbseg:
                maxidokulonbseg = ((self).jarmuvek[i+1].ido.idomasodpercben() - self.jarmuvek[i].ido.idomasodpercben())
                kezdoido = self.jarmuvek[i].ido
                vegido = self.jarmuvek[i+1].ido
        print("4. feladat: A leghosszabb forgalommentes időszak:",kezdoido,"-",vegido,".")

    def feladat5(self):

        """A járművek keresése"""

        rendszam = input("5. feladat: Adja meg a keresett rendszámot: ").strip()
        rendszamok = []
        if len(rendszam) != 7:
            print("Nem haladt el ilyen rendszámmal jármű.")
            return
        else:
            for jarmu in self.jarmuvek:
                jorendszam = True
                for i in range(0, 7):
                    if rendszam[i] != jarmu.rendszam[i] and rendszam[i] != "*":
                        jorendszam = False
                if jorendszam:
                    rendszamok.append(jarmu.rendszam)
        if len(rendszamok) == 0:
            print("Nem haladt el ilyen rendszámmal jármű.")
        else:
            for rendsz in rendszamok:
                print(rendsz)

    def feladat6(self):

        """Fájlba-írás"""

        print("6. feladat: Az ellenőrzések adatainak kiíratása.")
        kezdoora = self.jarmuvek[0].ido.ora
        f = open("ellenorzes.txt", "w",encoding="UTF-8")
        f.write(str(self.jarmuvek[0].ido.ora) + " óra: " + self.jarmuvek[0].rendszam + "\n")
        for jarmu in self.jarmuvek:
            if(jarmu.ido.ora > kezdoora):
                kezdoora = jarmu.ido.ora
                f.write(str(jarmu.ido.ora) + " óra: " + jarmu.rendszam + "\n")
        f.close()







