
public class Filme {
    private String titulo;
    private short anoLancamento;

    public Filme(String titulo, short anoLancamento){
        this.titulo = titulo;
        this.anoLancamento = anoLancamento;
    }

    public String toString(){
        return String.format("<Filme nome: %s, ano: %d>", this.titulo, this.anoLancamento);
    }

    public short getAnoLancamento(){
        return anoLancamento;
    }
}
