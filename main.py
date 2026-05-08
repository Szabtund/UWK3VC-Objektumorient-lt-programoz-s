from jarat import Belfoldijarat, Nemzetkozijarat
from legitarsasag import LegiTarsasag

legitarsasag: LegiTarsasag = LegiTarsasag("Blue Wings")

jarat1 = Belfoldijarat("B1993", "Budapest", 14000)
jarat2 = Belfoldijarat("B1992", "Per", 11000)
jarat3 = Nemzetkozijarat ("N2020","Malta", 21000)

legitarsasag.jarat_hozzaadas(jarat1)
legitarsasag.jarat_hozzaadas(jarat2)
legitarsasag.jarat_hozzaadas(jarat3)

legitarsasag.foglalas("Anna","B1993","2026-05-10")
legitarsasag.foglalas("Emma","B1992","2026-05-22")
legitarsasag.foglalas("Eva","N2020", "2026-05-15")
legitarsasag.foglalas("Zoltan","B1993", "2026-06-01")
legitarsasag.foglalas("Tunde", "N2020", "2026-05-29")
legitarsasag.foglalas("Attila","B1992","2026-05-20")

while True:
    print("\n--- Repulojegy Foglalasi Rendszer ---")
    print("1 - Jegy foglalasa")
    print("2 - Foglalas lemondasa")
    print("3 - Foglalasok listazasa")
    print("0 - Kilépés")

    valasztas = input(" Valassz egy menupontot")

    try:
        if valasztas == "1":
            utasnev = input("Add meg az utas nevet:")
            jaratszam = input("Add meg az jaratszamot:")
            datum = input("Add meg az datumot:")
            eredmeny = legitarsasag.foglalas(utasnev, jaratszam, datum)

            print(eredmeny)

        elif valasztas == "2":
            utasnev = input("Add meg az utas nevet:")
            jaratszam = input("Add meg az jaratszamot:")
            datum = input("Add meg az datumot:")
            eredmeny = legitarsasag.foglalas(utasnev, jaratszam, datum)
            print(eredmeny)

        elif valasztas == "3":
            legitarsasag.foglalasok_listazasa()

        elif valasztas == "0":
            print("Bye")
            break

        else:
            print("Hibas menupont")

    except ValueError as hiba:
        print(f"Hiba: {hiba}")




