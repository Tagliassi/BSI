import java.util.ArrayList;

public class Pasta {

    private ArrayList<Arquivo> arquivos;
    private String nome;

    public Pasta(String nome){
        this.nome = nome;
        this.arquivos = new ArrayList<>();
    }
    
    public void adicionaArquivo(Arquivo a){
        this.arquivos.add(a);
    }
}

class Disco{

}