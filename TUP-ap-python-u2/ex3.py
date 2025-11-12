# 3) Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.


def cambio(total, pago): 
    vuelto = pago - total 
    if vuelto < 0 :
        print(f"El pago es insuficiente, falta: ${vuelto}")
        return 
    elif vuelto == 0 :
        print("El pago es justo, no es necesario dar vuelto")
        return
    else :
        print(f"El vuelto total es: ${vuelto}")
    
    billetes = [500, 100, 50, 20, 10, 5, 1]

    for billete in billetes : 
        n = vuelto // billete
        if n > 0:
            print(f"{n} billete de ${billete}")
        vuelto %= billete 
    
   
## Ingresar dos numeros enteros: total compra y dinero recibido
total_compra= int(input("Ingrese el total de la compra: "))
pago_recibido= int(input("Ingrese el dinero recibido: "))

cambio(total_compra, pago_recibido)