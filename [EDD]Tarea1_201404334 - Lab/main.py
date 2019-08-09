from doble import Doble





class clasePrincipal:
    def metodoUnico(self):
        print("ads")
        Doble().imprimir()

        # 5 INSERCIONES AL INICIO
        Doble().insertar_inicio(10)
        Doble().insertar_inicio(20)
        Doble().insertar_inicio(30)
        Doble().insertar_inicio(40)
        Doble().insertar_inicio(50)
        Doble().imprimir()
        # 5 INSERCIONES AL FINAL
        Doble().insertar_final(100)
        Doble().insertar_final(200)
        Doble().insertar_final(300)
        Doble().insertar_final(400)
        Doble().insertar_final(500)
    # GRAFICAR
        #dob.Doble().graficar()
        # 5 INSERCIONES EN POSICIONES
        # GRAFICAR
        #dob.Doble().graficar()
        # OBTENER VALOR
        # ELIMINAR POR MEDIO DEL INDICE
        # GRAFICAR
        #dob.Doble().graficar()
        Doble().imprimir()

if __name__ == "__main__":
    cp = clasePrincipal()
    cp.metodoUnico()
