def hanyados(szam:int = 1, szam2:int = 1):
    if szam2 == 0:
        print("0-val nem lehet osztani!")
    else:
        osszeg: float = szam / szam2
        print(f"{szam} / {szam2} = {osszeg:.2f}")
    