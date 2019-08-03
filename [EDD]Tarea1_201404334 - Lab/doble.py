id=0
class Nodo:
    def __init__ (self, Id = None, Valor = None):
        self.id = Id
        self.valor = Valor
        self.siguiente = None
        self.anterior = None
    

class Doble:
    #id=0
    def __init__ (self):
        self.inicio = None
        self.fin = None

    def estavacia(self):
        if self.inicio==None:
            return True
        else:
            return False 

    def insetar_inicio(self,valor):
        global id
        print(id)
        nuevo=Nodo(id,valor)
        if self.inicio==None:
            self.fin=nuevo
        else:
            nuevo.siguiente=self.inicio
            self.inicio.anterior=nuevo
        self.inicio=nuevo        
        id+=1
        print("id: "+str(nuevo.id)+" valor: "+str(nuevo.valor))
        
        print(id)
    def insetar_final(self,valor):
        global id
        nuevo=Nodo(id,valor)
        if self.inicio==None:
            self.inicio=nuevo
        else:
            self.inicio.siguiente=nuevo
            nuevo.anterior=self.inicio
        self.fin=nuevo        
        id+=1
    def insetar_pos(self,index,valor):
        print("a")
    def obtener_pos(self,index):
        print("a")
    def eliminar(self,index): 
        print("a")
    def graficar(self):
        print("a")

      
    def imprimir(self):
        if self.inicio==None:
            print("Lista vacia")
        else:
            aux = self.inicio
            while aux != self.fin:
                print(str(aux.id) +" "+ aux.nombre)
                aux = aux.siguiente
    
if __name__ == "__main__":
    dob=Doble()
    dob.imprimir()
    dob.insetar_inicio(5)
    dob.imprimir()