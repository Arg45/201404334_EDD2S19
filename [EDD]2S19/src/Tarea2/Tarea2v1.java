package Tarea2;

import java.util.Scanner;

public class Tarea2v1 {
    //clase Bolsa
    Elemento inicio,fin;
    Scanner entrada;
    int op;

    public Tarea2v1() {
        op=0;
        entrada = new Scanner(System.in);
    }    
    public void menu(){
        String in;
        System.out.println("------------------------------------------\n"
                         + "Bienvenido al menu\n"
                         + "Por favor seleccione la opcion que desea:\n"
                         + " 1. Insertar\n"
                         + " 2. Contar\n"
                         + " 3. Salir");
        in=entrada.nextLine();
        if(validarNumero(in)){
            op=Integer.parseInt(in);        
            switch(op){
                case 1:
                    menuI();
                    break;
                case 2:
                    cuantos();
                    break;
                case 3:
                    System.exit(0); 
                    break;
                default:
                    System.out.println("------------------------------------------\n"
                                     + "La opcion seleccionada no es valida");
                    menu();
            }
        }else{
            System.out.println("------------------------------------------\n"
                             + "La opcion seleccionada no es valida");
            menu();
        }
        op=3;
        menu();
    }
    public void menuI(){
        System.out.println("Por favor, ingrese los siguientes datos.");
        System.out.println("ID: ");
        String in = entrada.nextLine();
        if(!validarNumero(in)){
            System.out.println("------------------------------------------\n"
                             + "El valor ingresado no es valido");
        }
        int ID = Integer.parseInt(in);
        System.out.println("Item: ");
        String item = entrada.nextLine();
        if(existe(ID)){
            System.out.println("------------------------------------------\n"
                             + "Error, Elemento existente.");
        }else{
            Elemento b = new Elemento(ID, item);
            insertar(b);
            System.out.println("------------------------------------------\n"
                             + "Insertado con exito!");
        }
    }
    public void insertar(Elemento nuevo){
        if(estaVacia()){
            inicio=nuevo;
            inicio.setSiguiente(inicio);
        }else{
            if(inicio.getSiguiente()==inicio){
                nuevo.setSiguiente(inicio);
                inicio.setSiguiente(nuevo); 
            }else{
                fin.setSiguiente(nuevo);
                nuevo.setSiguiente(inicio);    
            }
        }
        fin=nuevo;
    }
    public boolean estaVacia(){
        return inicio==null;
    }     
    public void cuantos(){
        if(estaVacia()){
            System.out.println("------------------------------------------\n"
                             + " Error, No existen elementos insertados.");
        }else{
            int i;
            i = 0;
            Elemento temp = inicio;
            System.out.println("------------------------------------------");
            do{
                System.out.println("ID: "+temp.getID()+" Item: "+temp.getItem());
                temp = temp.getSiguiente();
                i++;
            }while(temp != inicio);
            System.out.println(" \nExiste/n: "+i+" elemento/s");
        }        
    }
    
    private boolean validarNumero(String num){
        try {
            Integer.parseInt(num);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    boolean existe(int id){
        if(inicio != null){
            Elemento act = inicio;
            while(act!=null){
                if(act.getID()== id){
                    return true;
                }else{
                    act=act.getSiguiente();
                }
            }
        }
        return false;
    }
    public static void main(String[] args) {
        Tarea2v1 t2=new Tarea2v1();
        t2.menu();
    }
}
