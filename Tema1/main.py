# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def desglosarBilletes ( cantidad, tamanioBilletes):
    if cantidad >= tamanioBilletes:
        tipo = "billete"
        tipos = "billetes"
        if tamanioBilletes < 5:
            tipo = "moneda"
            tipos = "monedas"
        if cantidad//tamanioBilletes > 1:
            print(str(cantidad//tamanioBilletes) + " " + tipos + " de ", str(tamanioBilletes))
        else:
            print(str(cantidad//tamanioBilletes) + " " + tipo + " de ", str(tamanioBilletes))
        cantidad %= tamanioBilletes
    return cantidad


tiposBilletes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
print("Introduce un valor: ")
cambio = int(input())

i = 0
while cambio >0:
    billete = tiposBilletes[i]
    cambio = desglosarBilletes(cambio,billete)
    i+=1
