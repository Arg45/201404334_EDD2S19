import doble as dob       

class clasePrincipal:
    def metodoUnico(self):
        print("ads")

        dob.Doble().imprimir()
        # 5 INSERCIONES AL INICIO
        dob.Doble().insertar_inicio(10)
        dob.Doble().insertar_inicio(20)
        dob.Doble().insertar_inicio(30)
        dob.Doble().insertar_inicio(40)
        dob.Doble().insertar_inicio(50)
        dob.Doble().imprimir()
        # 5 INSERCIONES AL FINAL
        """dob.Doble().insertar_final(100)
        dob.Doble().insertar_final(200)
        dob.Doble().insertar_final(300)
        dob.Doble().insertar_final(400)
        dob.Doble().insertar_final(500)"""
    # GRAFICAR
        #dob.Doble().graficar()
        # 5 INSERCIONES EN POSICIONES
        # GRAFICAR
        #dob.Doble().graficar()
        # OBTENER VALOR
        # ELIMINAR POR MEDIO DEL INDICE
        # GRAFICAR
        #dob.Doble().graficar()

if __name__ == "__main__":
    cp = clasePrincipal()
    cp.metodoUnico()
