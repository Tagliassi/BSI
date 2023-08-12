package src;

class Produtos {
    private String nome, categoria;
    private double preco;

    // Construtor padrão vazio
    public Produtos() {
        // Não é necessário adicionar nada aqui
    }

    // Construtor
    public Produtos(String nome, double preco, String categoria) {
        this.nome = nome;
        this.preco = preco;
        this.categoria = categoria;
    }

    // Método para exibir informações gerais do produto
    public void exibirDetalhes() {
        System.out.println("Nome: " + nome);
        System.out.println("Preço: $" + preco);
        System.out.println("Categoria: " + categoria);
    }
}

class Smartphone extends Produtos {
    String tela;
    int camera;
    String processador;
    int armazenamento;

    // Construtor
    public Smartphone(String nome, double preco, String tela, int camera, String processador, int armazenamento) {
        this.tela = tela;
        this.camera = camera;
        this.processador = processador;
        this.armazenamento = armazenamento;
    }

    // Métodos para ações específicas de smartphone
    public void tirarFoto() {
        // Implementação
    }

    public void fazerChamada() {
        // Implementação
    }

    public void navegarInternet() {
        // Implementação
    }
}
