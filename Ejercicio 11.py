dinero = float(input("Deposita una cantidad de dinero:"))
a1 = dinero + dinero * 0.04
a2 = a1 + a1 * 0.04
a3 = a2 + a2 * 0.04
a1 = round(a1,2)
a2 = round(a2,2)
a3 = round(a3,2)
print("Tu cantidad de ahorro el primer año es de:", a1)
print("Segundo año:", a2)
print("Tercer año:", a3)
input()