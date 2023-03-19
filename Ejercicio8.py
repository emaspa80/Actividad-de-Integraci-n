#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:  Un constructor.  Los setters y getters para el nuevo atributo.  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

from Ejercicio7 import Cuenta
class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    
    @property    #getter
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    def mostrar(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"
   
    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)
