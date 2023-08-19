public class Lutador {
    private String nome, nacionalidade, categoria;
    private int idade, vitorias, derrotas, empates;
    private float altura, peso;

    public Lutador(String nome, String nacionalidade, int idade, float altura, float peso, int vitorias, int derrotas, int empates) {
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.idade = idade;
        this.altura = altura;
        this.setPeso(peso);
        this.vitorias = vitorias;
        this.derrotas = derrotas;
        this.empates = empates;
    }

    public void apresentar(){

        System.out.println("Nome: "+ this.getNome());
        System.out.println("Nacionalidade: "+ this.getNacionalidade());
        System.out.println("Idade: "+ this.getIdade());
        System.out.println("Altura: "+ this.getAltura());
        System.out.println("Peso em kg: "+ this.getPeso());
        System.out.println("Ganhou: "+ this.getVitorias());
        System.out.println("Perdeu: "+ this.getDerrotas());
        System.out.println("Empatou: "+ this.getEmpates());

    }

    public void status(){

        System.out.println(getNome());
        System.out.println("É um peso: " + getCategoria());
        System.out.println(getVitorias() + " Vitórias");
        System.out.println(getDerrotas() + " Derrotas");
        System.out.println(getEmpates() + " Empates");

    }

    public void ganharLuta(){

        this.setVitorias(this.getVitorias()+1);
        
    }

    public void perderLuta(){

        this.setDerrotas(this.getDerrotas()+1);
        
    }

    public void empatarLuta(){

        this.setEmpates(this.getEmpates()+1);
        
    }

    public float getAltura() {
        return altura;
    }

    public String getCategoria() {
        return categoria;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public int getIdade() {
        return idade;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public String getNome() {
        return nome;
    }

    public float getPeso() {
        return peso;
    }

    public int getVitorias() {
        return vitorias;
    }
    
    public void setAltura(float altura) {
        this.altura = altura;
    }

    private void setCategoria() {

        if(this.getPeso()<52.2){
            this.categoria = "Inválido";
        }
        else if (this.getPeso()<=70.3){
            this.categoria = "Leve";
        }
        else if (this.getPeso()<=83.9){
            this.categoria = "Médio";
        }
        else if (this.getPeso()<=120.2){
            this.categoria = "Pesado";
        }
        else {this.categoria = "Inválido";}

    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setPeso(float peso) {
        this.peso = peso;
        this.setCategoria();
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }
    
    
}
