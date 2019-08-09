from doble import Doble
from os import system

class clasePrincipal:
    def metodoUnico(self):
        print("ads")
        Doble().imprimir()
        # 5 INSERCIONES AL INICIO
        Doble().insertar_inicio(10)
        Doble().insertar_inicio(20)
        Doble().imprimir()
    def prueba1(self):
        print("a")
        Doble().imprimir()
        Doble().imprimirInicio()
if __name__ == "__main__":
    cp = clasePrincipal()
    cp.prueba1()
