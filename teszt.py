## eljárásaink tesztelése
import eljarasok

## Tesztesetek
print("1. teszteset: Pozitív számok")
eljarasok.hanyados(3, 5)

print("2. tesztesetek: Negatív számok")
eljarasok.hanyados(-5, -2)

print("3. teszteset: Tört számok (nem jó)")
## eljarasok.hanyados(-5.2, -2.2)
print("4. teszteset: Nincs paraméter")
eljarasok.hanyados()
print("5. teszteset: A nevező 0, b = 0")
eljarasok.hanyados(5, 0)
print("6. teszteset: A számláló 0, a = 0")
eljarasok.hanyados(0, 5)