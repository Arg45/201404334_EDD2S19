package Tarea2;

public class Tarea2 {
    Bolsa inicio;
    
    public void bolsavacia(){
    
    }
    public void insertar(Bolsa b){
        
    }
    public boolean estaVacia(){
        return inicio==null;
    }     
    public void cuantos(){
    
    }
            
    public static void main(String[] args) {
        Tarea2 t2=new Tarea2();
        
    }
}

//Tipo Bolsa (Elemento)
//Sintaxis
//- bolsavacia = Bolsa
//- insertar(Bolsa,Elemento) = Bolsa
//- esvacia(Bolsa) = booleano               listo
//- cuantos(Bolsa,Elemento) = natural
//Semántica 
//- esvacia(bolsavacia) = cierto
//- esvacia(poner(b,e)) = falso
//- cuantos(bolsavacia,e) = cero
//- cuantos(poner(b,f),e) = si f=e  sucesor(cuantos(b,e)) | cuantos(b,e)