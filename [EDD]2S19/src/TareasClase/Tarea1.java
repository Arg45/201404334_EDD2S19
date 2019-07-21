package TareasClase;

import java.util.Scanner;

public class Tarea1 {
    Scanner entrada;
    int op;
    String[] diaSemana;

    public Tarea1() {
        op=0;
        entrada = new Scanner(System.in);
        diaSemana = new String[7];
        diaSemana[0]="Domingo";
        diaSemana[1]="Lunes";
        diaSemana[2]="Martes";
        diaSemana[3]="Miercoles";
        diaSemana[4]="Jueves";
        diaSemana[5]="Viernes";
        diaSemana[6]="Sabado";  
    }
    
    public void menu(){
        String in;
        System.out.println("------------------------------------------\n"
                         + "Bienvenido al menu\n"
                         + "Por favor seleccione la opcion que desea:\n"
                         + " 1. Dia de la semana\n"
                         + " 2. Criba de Eratostenes\n"
                         + " 3. Salir");
        in=entrada.nextLine();
        if(validarNumero(in)){
            op=Integer.parseInt(in);        
            switch(op){
                case 1:
                    menuD();
                    break;
                case 2:
                    menuCE();
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
        op=0;
        menu();
    }
    public void menuCE(){
        String in;
        int n;
        System.out.println("------------------------------------------\n"
                         + "Bienvenido a Criba de Eratostenes\n"
                         + "Por favor ingrese un numero natural");
        in=entrada.nextLine();
        if(!validarNumero(in)){
            System.out.println("------------------------------------------\n"
                             + "El valor ingresado no es valido");
            menu();
        }
        n=Integer.parseInt(in);
        
        if(n>0){
            criba(n);
        }else{
            System.out.println("------------------------------------------\n"
                             + "El valor ingresado no es correcto\n"
                             + "Por favor ingrese un numero natural");
            menuCE();
        }
    }
    public void menuD(){
        String in;
        int dia,mes,anio,result;           
        System.out.println("------------------------------------------\n"
                             + "Bienvenido a Dia de la semana\n"
                             + "Por favor ingrese una fecha (dd/mm/aaaa(\n"
                             + "Dia:");
        in=entrada.nextLine();
        if(!validarNumero(in)){
            System.out.println("------------------------------------------\n"
                             + "El valor ingresado no es valido");
            menu();
        }
        dia=Integer.parseInt(in);
        System.out.println("Mes:");
        in=entrada.nextLine();
        if(!validarNumero(in)){
            System.out.println("------------------------------------------\n"
                             + "El valor ingresado no es valido");
            menu();
        }
        mes=Integer.parseInt(in);
        System.out.println("Ano:");
        in=entrada.nextLine();
        if(!validarNumero(in)){
                System.out.println("------------------------------------------\n"
                                 + "El valor ingresado no es valido");
                menu();
        }
        anio=Integer.parseInt(in);
        
        if(dia > 0 && mes > 0 && anio > 0){
            result=((anio-1)%7+((anio-1)/4-(3*((anio-1)/100+1)/4))%7+mes+dia%7)%7;
            int i;
            for(i=0;i<diaSemana.length;i++){
                if(i==result){
                    System.out.println("\nEl dia de la semana que corresponde a la fecha: "
                            +dia+"/"+mes+"/"+anio+" es: "+diaSemana[i]);
                }
            }
        }else{
            System.out.println("------------------------------------------\n"
                             + "El valor ingresado no es valido");
            menuD();
        }    
    }
    public void criba(int n){        
        System.out.println("------------------------------------------\n"
                             + "Los numeros primos antes de: "+n
                             + " son: ");
        int i;
        for(i=2;i<=n;i++){
            if(i%7==1 || i%5==1 || i%3==1 || i%2==1){
                System.out.println(i);
            }
        }
    }
    
    private boolean validarNumero(String num){
        try {
            Integer.parseInt(num);
            return true;
        } catch (NumberFormatException e) {
//            System.out.println("Error "+e);
            return false;
        }
    }
}
