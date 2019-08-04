id=0
class Nodo:
    def __init__ (self, Id = None, Valor = None):
        self.id = Id
        self.valor = Valor
        self.siguiente = None
        self.anterior = None
    
class Doble:
    def __init__ (self):
        self.inicio = None
        self.fin = None
    
    def insertar_inicio(self,valor):
        global id
        #print(id)
        nuevo=Nodo(id,valor)
        if self.estavacia():
            self.fin=nuevo
        else:
            nuevo.siguiente=self.inicio
            self.inicio.anterior=nuevo
        self.inicio=nuevo        
        id+=1
        #print("id: "+str(nuevo.id)+" valor: "+str(nuevo.valor))        
        #print(id)
    def insertar_final(self,valor):
        global id
        #print(id)
        nuevo=Nodo(id,valor)
        if self.inicio==None:
            self.inicio=nuevo
        else:
            self.fin.siguiente=nuevo
            nuevo.anterior=self.fin
        self.fin=nuevo        
        id+=1
        #print("id: "+str(nuevo.id)+" valor: "+str(nuevo.valor))   
        #print(id)
    def insertar_pos(self,index,valor):
        if index<0:
            print("El valor ingresado no es valido.")
        else:
            if self.existe(index):
                aux=self.inicio
                while aux != None:
                    if aux.id==index:
                        aux.id=index
                        aux.valor=valor
                        break
                    else:
                        aux = aux.siguiente 
                print("Valor modificado/insertado exitosamente!")
            else:
                print("El valor ingresado no existe. No se puede insertar.")
    def obtener_pos(self,index):
        if index<0:
            print("El valor ingresado no es valido.")
        else:
            if self.existe(index):
                print("Valor encontrado!")
                self.imprimirNodo(index)
            else:
                print("El valor ingresado no existe.")
    def eliminar(self,index): 
        if index<0:
            print("El valor ingresado no es valido.")
        else:
            if self.existe(index):
                aux=self.inicio
                while aux != None:
                    if aux.id==index:
                        if aux.anterior==None:
                            self.inicio=self.inicio.siguiente
                            self.inicio.anterior=None
                            aux.siguiente=None
                            break
                        else:
                            aux.anterior.siguiente=aux.siguiente
                        if aux.siguiente==None:
                            self.fin=self.fin.anterior
                            self.fin.siguiente=None
                            aux.anterior=None
                        else:
                            aux.siguiente.anterior=aux.anterior
                        break
                    else:
                        aux = aux.siguiente 
                print("Valor eliminado!")
            else:
                print("El valor ingresado no existe.")
    def graficar(self):
        print("a")
      
    def imprimir(self):
        if self.inicio==None:
            print("Lista vacia")
        else:
            aux = self.inicio
            while aux != None:
                print("id: "+str(aux.id)+" valor: "+str(aux.valor)) 
                aux = aux.siguiente
    def imprimirInicio(self):
        print("inicio - id: "+str(self.inicio.id)+" valor: "+str(self.inicio.valor))
    def imprimirFin(self):
        print("   fin - id: "+str(self.fin.id)+" valor: "+str(self.fin.valor))
    def imprimirNodo(self,index):
        aux = self.inicio
        while aux != None:
            if index==aux.id:
                print("ID: "+str(aux.id)+" Valor: "+str(aux.valor)) 
                break
            else:
                aux = aux.siguiente

    def estavacia(self):
        if self.inicio==None:
            return True
        else:
            return False 
    def existe(self,index):
        aux = self.inicio
        while aux != None:
            if index==aux.id:
                return True
            else:
                aux = aux.siguiente
    
if __name__ == "__main__":    
    dob=Doble()
    
    dob.imprimir()
    dob.insertar_inicio(10)
    dob.insertar_inicio(20)
    dob.insertar_inicio(30)
    dob.insertar_inicio(40)
    dob.insertar_inicio(50)
    print("\n")
    dob.imprimir()
    print("\n")
    #dob.imprimirInicio()
    #dob.imprimirFin()
    #print("\n")
    dob.insertar_final(100)
    dob.insertar_final(200)
    dob.insertar_final(300)
    dob.insertar_final(400)
    dob.insertar_final(500)
    print("\n")
    dob.imprimir()
    print("\n")
    dob.insertar_pos(3,777)
    dob.insertar_pos(8,999)
    dob.insertar_pos(9,1000)
    dob.insertar_pos(100,1000000000)
    print("\n")
    dob.imprimir()
    print("\n")
    #dob.imprimirInicio()
    #dob.imprimirFin()
    dob.obtener_pos(3)
    print("\n")
    dob.eliminar(0)
    dob.eliminar(4)
    dob.eliminar(9)
    print("\n")
    dob.imprimir()
    print("\n")


"""
    # 5 INSERCIONES AL INICIO
    dob.insertar_inicio(10)
    dob.insertar_inicio(20)
    dob.insertar_inicio(30)
    dob.insertar_inicio(40)
    dob.insertar_inicio(50)
    # 5 INSERCIONES AL FINAL
    dob.insertar_final(100)
    dob.insertar_final(200)
    dob.insertar_final(300)
    dob.insertar_final(400)
    dob.insertar_final(500)
    # GRAFICAR
    #dob.graficar()
    # 5 INSERCIONES EN POSICIONES
    dob.insertar_pos(3,777)
    dob.insertar_pos(8,999)
    # GRAFICAR
    #dob.graficar()
    # OBTENER VALOR
    dob.obtener_pos(3)
    # ELIMINAR POR MEDIO DEL INDICE
    dob.eliminar(0)
    dob.eliminar(4)
    # GRAFICAR
    #dob.graficar()
"""