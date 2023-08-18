public class Banco {
    private String nome;

    public Banco(String nome) {
        this.nome = nome;
    }

    public boolean transferir(Cliente origem, Cliente destino, double valor) {
        if ((float)(origem.getSaldo() - valor) < 0) {
            System.out.printf("[ Banco %s ] Saldo insuficiente na conta de origem (%s)\n", this.nome, origem.getNome());
            return false;
        }

        origem.sacar(valor);
        destino.depositar(valor);

        System.out.printf("[ Banco %s ] Cliente %s transferiu o valor de R$%.2f para o cliente %s\n", this.nome, origem.getNome(), valor, destino.getNome());
        return true;
    }
}
