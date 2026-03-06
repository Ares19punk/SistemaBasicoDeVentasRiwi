# 491-captura-de-datos

print("-"*35)
print("Sistema de venta RiwiTechStories")
print("-"*35)
print(".:Datos generales:.")
nombre = str(input("Nombre del cliente: "))
precio_unit = float(input("Digite precio del producto: "))
cantidad_pro = float(input("DIgite la cantidad: "))

while True:
    print("Por favor seleccione una opción correcta: ")
    print("1. CLiente VIP")
    print("2. Cliente Regular")
    option_vip = input("Digite la opción: ")
    if option_vip == "1" or option_vip == "2":
        break
    else:
        print("")
        print("❌ Error: opción no válida")
        





