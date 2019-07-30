package Ejercicios;

import java.util.Scanner;

public class Ejercicio1 {
    Estudiante_E1 inicio,fin;
    
    Scanner entrada = new Scanner(System.in);
    
    public void menu(){
        System.out.println("--------------------------------------------\n"
                         + "Bienvenido al Ejercicio 1, Lista de estudiantes \n"
                         + "Por favor, seleccione una de las opciones: \n"
                         + " 1. Insertar\n"
                         + " 2. Eliminar\n"
                         + " 3. Mostrar\n"
                         + " 4. Salir");        
        String op;
        op = entrada.nextLine();
        if(validarNumero(op)){
            int opSeleccionada = Integer.parseInt(op);            
            switch(opSeleccionada){
                case 1:    
                    menuI();
                    break;
                case 2:    
                    desencolar();
                    break;
                case 3:  
                    if(estaVacia()){
                        System.out.println("--------------------------------------------\n"
                                         + "La cola esta vacia."); 
                    }else{
                        print();            
                    }                    
                    break;
                case 4:
                    System.exit(0); 
                    break;
                default:
                    System.out.println("--------------------------------------------\n"
                            + "El valor ingresado no es valido"); 
                    menu();
                    break;                        
            }        
        }else{
           System.out.println("--------------------------------------------\n"
                            + "El valor ingresado no es valido\n"); 
           menu();
        }
        menu();
    }
    public void menuI(){
        System.out.println("--------------------------------------------\n"
                         + "Ingrese los siguientes datos:\n"
                         + " Carnet:"); 
        String op;
        op = entrada.nextLine();
        int carnet;
        if(!validarNumero(op)){
            System.out.println("--------------------------------------------\n"
                             + "El valor ingresado no es valido\n"); 
            menu();
        }
        carnet = Integer.parseInt(op);
        System.out.println(" Nombre:");
        String nombre = entrada.nextLine();
        System.out.println(" Apellido:");
        String apellido = entrada.nextLine();
        Estudiante_E1 n = new Estudiante_E1(nombre, apellido, carnet);
        encolar(n);
        System.out.println("--------------------------------------------\n"
                          +nombre+" "+apellido+" ha sido ingresado exitosamente."); 
    }
    
    public void encolar(Estudiante_E1 nuevo){
        if(existe(nuevo.getCarnet())){
            System.out.println("--------------------------------------------\n"
                             + "El estudiante ya esta registrado."); 
            menu();
        }else{
            if(estaVacia()){
                inicio=nuevo;
            }else{
                fin.setSiguiente(nuevo);
            }
            fin=nuevo;
        }
    }
    public void desencolar(){
        if(estaVacia()){
            System.out.println("--------------------------------------------\n"
                            + "La cola esta vacia."); 
        }else{
            System.out.println("--------------------------------------------\n"
                            + inicio.getNombre()+" "+inicio.getApellido() +" ha sido eliminado exitosamente."); 
            inicio=inicio.getSiguiente();            
        }
    }
    public void print(){
        Estudiante_E1 temp = inicio;
        System.out.println("--------------------------------------------");
        while (temp!=null) {
            System.out.println("Carnet: "+temp.getCarnet()+" Nombre: "+temp.getNombre()+" Apellido: "+ temp.getApellido());
            temp=temp.getSiguiente();            
        }
    }
    
    public boolean estaVacia(){
        return inicio==null;
    }
    boolean existe(int id){
        if(inicio != null){
            Estudiante_E1 act = inicio;
            while(act!=null){
                if(act.getCarnet()== id){
                    return true;
                }else{
                    act=act.getSiguiente();
                }
            }
        }
        return false;
    }
        
    private boolean validarNumero(String num){
        try {
            Integer.parseInt(num);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    
    public static void main(String[] args) {
        Ejercicio1 e1 = new Ejercicio1();
        e1.menu();
    }
}
