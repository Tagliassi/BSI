import java.util.ArrayList;

public class Compactado extends Arquivo {

    private ArrayList<Arquivo> arquivos;

    public Compactado(){
        this.arquivos = new ArrayList<>();
    }

    public void adicionaArquivo(Arquivo a){
        this.arquivos.add(a);
    }

    public void mostrar(){
        System.out.println("Mostrando");
    }    
    
}
