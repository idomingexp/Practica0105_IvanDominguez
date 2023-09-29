total = float(input("Cuantas barras se han vendido:"))
barrasv = float(input("CUantas barras viejas se han vendido:"))
print("Una barra vale 3.49€")
print("Por no ser fresca se aplica un descuento del 60%")
dinero = (total - barrasv) * 3.49 + (barrasv * 0.6) * 3.49
print("Ganancia total final:", dinero, "€")
input()
