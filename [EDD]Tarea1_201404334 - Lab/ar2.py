from os import system
class Nodo:
    def __init__ (self, Id = None, Valor = None):
        self.id = Id
        self.valor = Valor
        self.siguiente = None
id=0
class Doble:    
    def __init__ (self):
        self.inicio = None
        self.fin = None
    def metodounico(self):
        print("\"metodo de otro archivo tipo .py\"")
    def insertar_inicio(self,valor):
        global id
        nuevo=Nodo(id,valor)
        if self.inicio==None:
            self.fin=nuevo
        else:
            nuevo.siguiente=self.inicio
            self.inicio.anterior=nuevo
        self.inicio=nuevo        
        id+=1
        #print("id: "+str(nuevo.id)+" valor: "+str(nuevo.valor))        
        #print(id)
    def imprimir(self):
        if self.inicio==None:
            print("Lista vacia")
        else:
            aux = self.inicio
            while aux != None:
                print("id: "+str(aux.id)+" valor: "+str(aux.valor)) 
                aux = aux.siguiente