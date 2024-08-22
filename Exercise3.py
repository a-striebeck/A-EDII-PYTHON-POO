class Animal:
    def __init__(self, name=""):
        self._name = name  # Atributo encapsulado

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def talk(self):
        pass

    def move(self):
        pass

    def describe(self):
        return f"{self.name} es un animal."

    @classmethod
    def base(cls):
        return cls.__bases__

    @classmethod
    def show_subclasses(cls):
        return cls.__subclasses__()

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} es un perro.")

    @property
    def description(self):
        return f"Perro llamado {self.name}"

    @description.setter
    def description(self, value):
        self.name = value

    def talk(self):
        print('Guau')

    def move(self):
        print("Caminando en cuatro patas")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} es una vaca")

    @property
    def description(self):
        return f"Vaca llamada {self.name}"

    @description.setter
    def description(self, value):
        self.name = value

    def talk(self):
        print("Muuu!")

    def move(self):
        print("Caminando en cuatro patas")

class Bee(Animal):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} es una abeja")

    @property
    def description(self):
        return f"Abeja llamada {self.name}"

    @description.setter
    def description(self, value):
        self.name = value

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
    print(f"{dog.name} dice: ", end="")
    dog.talk()
    print(f"{dog.name} se mueve: ", end="")
    dog.move()

    print(f"{cow.name} dice: ", end="")
    cow.talk()
    print(f"{cow.name} se mueve: ", end="")
    cow.move()

    print(f"{bee.name} dice: ", end="")
    bee.talk()
    print(f"{bee.name} se mueve: ", end="")
    bee.move()

    # Mostrar herencia
    print("\nClases base de Dog:", Dog.base())
    print("Subclases de Animal:", Animal.show_subclasses())

    # Usar @property y @setter
    print(dog.description)  
    dog.description = "Max" 
    print(dog.description)  

if __name__ == "__main__":
    main()
