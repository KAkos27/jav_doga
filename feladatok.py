import math
import random


def nev_bekeres():
    elso_b = "b"
    while elso_b != "A":
        nev: str = str(input("Kérek egy nevet: "))
        elso_b = nev[0]


def ottel_oszthatok():
    osszegzo: int = 0
    for i in range(0, 5, 1):
        szam: int = math.floor(random.random() * 21 + 30)
        if szam % 5 == 0:
            osszegzo += 1
    return osszegzo


def szoveges(text: str, n: int):
    print(text[1] * n)


def szam_megadas():
    szam: int = 1
    osszegzo: int = -1
    while szam != 0:
        szam: int = int(input("Kérek egy számot!: "))
        osszegzo += 1
    return osszegzo


def szamkitalalo():
    print("_________________________________")
    print("\tSZÁMKITALÁLÓ")
    f_tipp = szam_bekeres()

    gep_tipp = math.floor(random.random() * 91 + 10)

    while f_tipp != gep_tipp:
        if gep_tipp > f_tipp:
            print("Nagyobbra gondoltam")
            f_tipp = szam_bekeres()
        else:
            print("Kisebbre gondoltam")
            f_tipp = szam_bekeres()

    print("Nyertél")


def szam_bekeres():
    f_tipp: int = 0
    while f_tipp < 10 or 100 < f_tipp:
        f_tipp = int(input("Kérek egy számot!: "))
    return f_tipp

