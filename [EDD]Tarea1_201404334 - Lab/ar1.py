#import ar2 as a2
from ar2 import laotraclase as a2

class pruebaImportarArchivos:
    def m(self):
        print("metodo en el mismo archivo")

        #a2.laotraclase.metodounico(self)
        a2.metodounico(self)

if __name__ == '__main__':
    e=pruebaImportarArchivos()
    e.m()
    #print("\n")
    #a2.metodounico(self)

    #a2.metodounico()

    