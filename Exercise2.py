# 2. Desarrollar una APP por consola que Cree una estructura como la de la  inheritance-exercise.
#     a.    Implementar la Herencia
#     b.    Implementar __bases__ y __subclases__
#     c.    Implementar base()
#     d.    Crear Objetos y mostrar por consola. 

class Animal:
    Name = ""

    def __init__(self, name=""):
        self.Name = name

    def talk(self):
        pass

    def move(self):
        pass

    def describe(self):
        return f"{self.Name} es un animal."

    @classmethod
    def base(cls):
        return cls.__bases__

    @classmethod
    def show_subclasses(cls):
        return cls.__subclasses__()

class Dog(Animal):
    def __init__(self, tName):
        super().__init__(tName)
        print(f"{self.Name} es un perro.")

    def talk(self):
        print('Guau')

    def move(self):
        print("Caminando en cuatro patas")

class Cow(Animal):
    def __init__(self, tName):
        super().__init__(tName)
        print(f"{self.Name} es una vaca")

    def talk(self):
        print("Muuu!")

    def move(self):
        print("Caminando en cuatro patas")

class Bee(Animal):
    def __init__(self, tName):
        super().__init__(tName)
        print(f"{self.Name} es una abeja")

    def talk(self):
        print("BZZZZ")

    def move(self):
        print("Volando")

def main():
    # Crear instancias de las clases
    dog = Dog("Rex")
    cow = Cow("Bessie")
    bee = Bee("Buzz")

    # Mostrar comportamiento
    print(f"{dog.Name} dice: ", end="")
    dog.talk()
    print(f"{dog.Name} se mueve: ", end="")
    dog.move()

    print(f"{cow.Name} dice: ", end="")
    cow.talk()
    print(f"{cow.Name} se mueve: ", end="")
    cow.move()

    print(f"{bee.Name} dice: ", end="")
    bee.talk()
    print(f"{bee.Name} se mueve: ", end="")
    bee.move()

    # Mostrar herencia
    print("\nClases base de Dog:", Dog.base())
    print("Subclases de Animal:", Animal.show_subclasses())

if __name__ == "__main__":
    main()
