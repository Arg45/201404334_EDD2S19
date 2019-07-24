package Tarea2;

public class Bolsa {
    private int ID;
    private String item;
    private Bolsa siguiente;

    public Bolsa(int ID, String item) {
        this.ID = ID;
        this.item = item;
        this.siguiente = null;
    }

    /**
     * @return the ID
     */
    public int getID() {
        return ID;
    }

    /**
     * @param ID the ID to set
     */
    public void setID(int ID) {
        this.ID = ID;
    }

    /**
     * @return the item
     */
    public String getItem() {
        return item;
    }

    /**
     * @param item the item to set
     */
    public void setItem(String item) {
        this.item = item;
    }

    /**
     * @return the siguiente
     */
    public Bolsa getSiguiente() {
        return siguiente;
    }

    /**
     * @param siguiente the siguiente to set
     */
    public void setSiguiente(Bolsa siguiente) {
        this.siguiente = siguiente;
    }
    
}
