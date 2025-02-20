# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    # Check if the input is a positive integer
    if not isinstance(numero, int) or numero < 1:
        return None

    # Initialize the result to 1
    result = 1

    # Calculate the factorial
    for i in range(1, numero + 1):
        result *= i

    return result

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    # Check if the input is an integer
    if not isinstance(valor, int):
        return None

    # 1 and numbers less than 1 are not prime
    if valor <= 1:
        return False

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(valor**0.5) + 1):
        if valor % i == 0:
            return False

    return True
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
class Animal:
    def __init__(self, especie, color):
        # Initialize attributes
        self.Edad = 0
        self.Especie = especie
        self.Color = color

    def CumplirAnios(self):
        # Increment the age by 1 and return the new age
        self.Edad += 1
        return self.Edad

def ClaseAnimal(especie, color):
    # Create an instance of the Animal class
    animal_instance = Animal(especie, color)
    return animal_instance


