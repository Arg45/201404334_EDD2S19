id=0
class Nodo:
    def __init__ (self, Id = None, Valor = None):
        self.id = Id
        self.valor = Valor
        self.siguiente = None
        self.anterior = None
class Doble():
    cod = 1
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
    
    def graficar1(self):
        import os as s

        a = open("grafo.dot","r")

        aux = self.inicio
        texto = "digraph G{\n"
        while aux is not None:
            if aux.siguiente is not None:                
                texto += str(aux.id)+" -> " +str(aux.siguiente.id)+"\n"
            if aux.anterior is not None:
                texto += str(aux.id)+" -> " +str(aux.anterior.id)+"\n"
            texto += str(aux.id)+" [label=\" "+str(aux.valor)+" \"]\n"
            aux = aux.siguiente
        texto += "}"
        print(texto)
        
        a.write(texto)
        a.close()
        #s.system("START cmd.exe /K  \"CD C:\Program Files (x86)\Graphviz2.38\bin \"")
        #s.system("dot.exe -Tjpg grafo.dot -o imagen.jpg")
    def graficar2(self):
        from graphviz import Digraph as g
        dot = g(comment='The Round Table')
        aux = self.inicio
        texto = "digraph G{\nrankdir=LR\n"
        while aux is not None:
            dot.node(str(aux.id), str(aux.valor))
            
            if aux.siguiente is not None:                
                dot.edge(str(aux.id),str(aux.siguiente.id))
                texto += str(aux.id)+" -> " +str(aux.siguiente.id)+"\n"
            if aux.anterior is not None:
                dot.edge(str(aux.id),str(aux.anterior.id))
                texto += str(aux.id)+" -> " +str(aux.anterior.id)+"\n"
            texto += str(aux.id)+" [label=\" "+str(aux.valor)+" \"]\n"
            aux = aux.siguiente
        texto += "}"
        print(texto)
        #dot.render(filename="prueba.gv",directory="C:\Users\argue\OneDrive\Documents\NetBeansProjects",view=True,cleanup=False)
        dot.render('round-table.dot', view=True)
    def graficar3(self):
        from graphviz import Digraph as g
        dot = g(comment='Tarea 1 - Lab')
        aux = self.inicio
        while aux is not None:
            dot.node(str(aux.id), str(aux.valor))            
            if aux.siguiente is not None:                
                dot.edge(str(aux.id),str(aux.siguiente.id))
            if aux.anterior is not None:
                dot.edge(str(aux.id),str(aux.anterior.id))
            aux = aux.siguiente
        dot.render("tarea1_"+str(self.cod)+".dot", view=True)
        self.cod+=1

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
                print("--> ID: "+str(aux.id)+" Valor: "+str(aux.valor)) 
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
    
    def prueba(self):
        dob.imprimir()
        dob.insertar_inicio(10)
        dob.insertar_inicio(20)
        dob.insertar_inicio(30)
        dob.insertar_inicio(40)
        dob.insertar_inicio(50)
        dob.graficar2()
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
        dob.graficar2()
        print("\n")
        dob.imprimir()
        print("\n")
        dob.insertar_pos(3,777)
        dob.insertar_pos(8,999)
        #dob.insertar_pos(9,1000)
        dob.insertar_pos(100,1000000000)
        dob.graficar2()
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

        dob.graficar2()
if __name__ == "__main__":    
    dob=Doble()
    #dob.prueba()
    
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
    dob.graficar3() 
    # INSERTAR EN POSICIONES
    dob.insertar_pos(3,777)
    dob.insertar_pos(8,999)
    # GRAFICAR
    dob.graficar3() 
    # OBTENER EL VALOR DE LA LISTA
    dob.obtener_pos(2)
    # ELIMINAR POR MEDIO DEL INDICE
    dob.eliminar(0)
    dob.eliminar(4)
    # GRAFICAR
    dob.graficar3()
