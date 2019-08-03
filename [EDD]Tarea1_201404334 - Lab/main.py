#import doble as dob
# 5 INSERCIONES AL INICIO
# 5 INSERCIONES AL FINAL
# GRAFICAR
# 5 INSERCIONES EN POSICIONES
# GRAFICAR
# OBTENER VALOR
# ELIMINAR POR MEDIO DEL INDICE
# GRAFICAR
"""
i=0
class doble:
    
    def inc(self):
        print(i)
        global i
        i = 1
        print(i)
        

if __name__ == "__main__":
    dob=doble()
    dob.inc()
    """

mi_variable_global = 20
 
def una_funcion():
    global mi_variable_global #En este caso sí vamos a modificar a la global
    mi_variable_global = 10 #Ahora la variable es 10, no 20
    print("Una función, la variable global es: " + str(mi_variable_global))
 
def otra_funcion():
    print("Otra función, la variable global es: " + str(mi_variable_global))
 
una_funcion()
otra_funcion()