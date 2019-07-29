package Tarea2;

public class Elemento {
    private int ID;
    private String item;
    private Elemento siguiente;

    public Elemento(int ID, String item) {
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
    public Elemento getSiguiente() {
        return siguiente;
    }

    /**
     * @param siguiente the siguiente to set
     */
    public void setSiguiente(Elemento siguiente) {
        this.siguiente = siguiente;
    }
    
}
