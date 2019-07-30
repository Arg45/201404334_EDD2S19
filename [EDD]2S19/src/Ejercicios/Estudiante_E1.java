package Ejercicios;
public class Estudiante_E1 {
    private String nombre;
    private String apellido;
    private int carnet;
    private Estudiante_E1 siguiente;
    public Estudiante_E1(String nombre, String apellido, int carnet) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.carnet = carnet;
        this.siguiente = null;
    }
    /**
     * @return the nombre
     */
    public String getNombre() {
        return nombre;
    }
    /**
     * @param nombre the nombre to set
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    /**
     * @return the apellido
     */
    public String getApellido() {
        return apellido;
    }
    /**
     * @param apellido the apellido to set
     */
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    /**
     * @return the carnet
     */
    public int getCarnet() {
        return carnet;
    }
    /**
     * @param carnet the carnet to set
     */
    public void setCarnet(int carnet) {
        this.carnet = carnet;
    }
    /**
     * @return the siguiente
     */
    public Estudiante_E1 getSiguiente() {
        return siguiente;
    }
    /**
     * @param siguiente the siguiente to set
     */
    public void setSiguiente(Estudiante_E1 siguiente) {
        this.siguiente = siguiente;
    }    
}