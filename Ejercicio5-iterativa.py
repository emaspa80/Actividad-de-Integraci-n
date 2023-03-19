#5.Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva. 

def get_int():
    while True:
        user_input = input('Ingresa un numero entero:')
        try:
            value = int(user_input)
        except ValueError:
            print('No es un entero válido. ¡Pruébalo otra vez!')
        else:
            return value


get_int()