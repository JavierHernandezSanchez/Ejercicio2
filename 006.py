#!/usr/bin/python

#escribir un script que pregunte la edad del usuario y le devuelva un mensaje 
#original sobre lo que le ocurrirá cuando cumpla su edad + 5

edad = ""
while not edad.isnumeric():
    print("Hola, qué edad tienes? ", end="")
    edad = input()
    if not edad.isnumeric():
        print("Tienes que decir un número!")
edad_futura = int(edad) + 5
print(f"Dentro de 5 años tendrás {edad_futura} años y no estarás confinado")
