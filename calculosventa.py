#Calculo de subtotal

subtotal = precio_unit * cantidad_pro

#Descuento si aplica

if option_vip == "1":
    descuento = subtotal*0.1
else:
    print("Descuento no aplica")
    descuento = 0

total = subtotal - descuento