print("Ingresá tu edad")
edad=int(input())
if edad<0:
    OK=False
    print("Aun no naciste?")
else: OK=True
if OK:
    faltan=int(100-edad)
    if 0<faltan<=100 :  
        print("Te faltan " + str(faltan) + " años para cumplir 100 años")
    elif faltan==0:
        print("¡Tenes 100 años!")
    else:
        print("¡Ya cumpliste 100 años!")
