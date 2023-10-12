
# bizonyos műveletek ismétlésére való a ciklus
# cilusváltozó - számlálja, hogy hányszor futott le a ciklus
# ciklusmag - ismétlendő utasítások
# ciklusfeltétel - itt adjuk meg, hogy meddig fusson a ciklus
def szamlalos_ciklus1():
    cv: int = 1
    while (cv <= 10):
        print(f"{cv}Többé nem kések, mert lemaradok fontos információkról!")
        cv += 1

    print(cv, "A ciklus után")

## kérjünk be egy 10-nél nagyobb számot a felhasználótól

def eloltesztelos_ciklus():
    szam:int = int(input("Adjon meg egy 10-nél nagyobb számot: "))
    while szam <= 10:
        print("10-nél nagyobb számot szeretnék kérni!")
        szam:int = int(input("Adjon meg egy 10-nél nagyobb számot: "))

    print("HURRÁ!!! Végre sikerült 10-nél nagyobbat!", szam)


# készíts külön eljárást
# 1. Írd ki a számokat 1 és 10 között a képernyőre egymás mellé
def elso_feladat():
    cv: int = 1
    while(cv <= 10):
        print(f"{cv}", end = ", ")
        cv += 1

# 2. írd ki a számokat 20 és 30 között a képernyőre
def masodik_feladat():
    print("\n")
    cv: int = 20
    while(cv <= 30):
        print(f"{cv}", end = ", ")
        cv += 1
# 3. Írd ki a 15 és 25 közötti páros számokat
def harmadik_feladat():
    print("\n")
    cv: int = 15
    while (cv <= 25):
        if cv % 2 == 0:
            print(f"{cv}", end = ", ")
        cv += 1
        


    
# 4. Írd ki a számokat egyesével 12 és 30 között fordított sorrendbe
def negyedik_feladat():
    print("\n")
    cv: int = 30
    while(cv >= 12):
        print(f"{cv}", end = ", ")
        cv -= 1



