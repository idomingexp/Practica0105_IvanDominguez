invertir = float(input("Introduce dinero a invertir:"))
interes = float(input("Introduce interés anual:"))
años = int(input("Durante cuántos años es la inversión:"))
capital = invertir + (invertir * (años * interes / 100))
print("Tu capital obtenido es de:", capital, "€")
input()