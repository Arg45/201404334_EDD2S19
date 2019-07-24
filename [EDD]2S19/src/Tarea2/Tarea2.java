package Tarea2;

import java.util.Scanner;

public class Tarea2 {
    Bolsa inicio, fin;
    Scanner entrada;
    int op;

    public Tarea2() {
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
        int ID = entrada.nextInt();
        System.out.println("Item: ");
        String item = entrada.next();
        if(existe(ID)){
            System.out.println("Error, Nodo existente.");
        }else{
            Bolsa b = new Bolsa(ID, item);
            insertar(b);
            System.out.println("Insertado con exito!\n");
        }
    }
    public void bolsavacia(){
    
    }
    public void insertar(Bolsa nuevo){
        if(estaVacia()){
            inicio=nuevo;
        }else{
            fin.setSiguiente(nuevo);
        }
        fin=nuevo;
    }
    public boolean estaVacia(){
        return inicio==null;
    }     
    public void cuantos(){
        int i;
        i = 0;
        Bolsa temp = inicio;
        while(temp != null){
            System.out.println("ID: "+temp.getID()+" Item: "+temp.getItem());
            temp = temp.getSiguiente();
            i++;
        }
        System.out.println(" Existe/n: "+i+" elemento/s");
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
            Bolsa act = inicio;
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
        Tarea2 t2=new Tarea2();
        t2.menu();
    }
}

//Tipo Bolsa (Elemento)
//Sintaxis
//- bolsavacia = Bolsa
//- insertar(Bolsa,Elemento) = Bolsa
//- esvacia(Bolsa) = booleano               listo
//- cuantos(Bolsa,Elemento) = natural       listo, creo
//Semántica 
//- esvacia(bolsavacia) = cierto
//- esvacia(poner(b,e)) = falso
//- cuantos(bolsavacia,e) = cero
//- cuantos(poner(b,f),e) = si f=e  sucesor(cuantos(b,e)) | cuantos(b,e)