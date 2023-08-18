public class Agentes {
    private String nome;
    public Agentes(String nome) {
        this.nome = nome;
    }
    public String getNome(){
        return nome;
    }

    public String toString(){
            return String.format("<Agente nome: %s>", this.nome);
        }
}
