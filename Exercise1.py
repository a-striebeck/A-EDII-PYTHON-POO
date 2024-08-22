# 1. Crear una Clase en Python.
#     a.  Asignarles atributos de clase e instancia.
#     b.  Asignar métodos de Instancia, Clase y estáticos.

class Person(object):
    
    #Atributos de clase:
    species = "Humano"
    maxSpeed = "20 Km/h"

    #Metodo estatico
    @classmethod
    def showMaxSpeed(cls):
        print(f"La maxima velocidad que puede alcanzar un humano promedio es de {cls.maxSpeed}")
    
    #Metodo de
    @staticmethod
    def instanceSuccessfullMessage(value):
        if value == True:
            print("Persona instanciada satisfactoriamente.")
        else:
            print("No se pudo instanciar la persona.")


    def __init__(self, Name, LastName, Ocupation):
    
    #Atributos de instancia:
        self.name = Name
        self.lastName = LastName
        self.ocupation = Ocupation
        Person.instanceSuccessfullMessage(True)

    #Metodo de Instancia
    def introducePerson(self):
        print(f"{self.name} {self.lastName} es {self.ocupation}")
    



def main():
    #Creo la instancia de la clase Persona.
    Persona = Person("Pedro", "Pascal", "Actor")

    #LLamada a los metodos de instancia y la clase.
    Persona.introducePerson()
    Persona.showMaxSpeed()

if __name__ == "__main__":
    main()
    



    