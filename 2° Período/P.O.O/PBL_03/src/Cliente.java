public class Cliente {
    private String nome;
    private double saldo;

    public Cliente(String nome, double saldoInicial) {
        this.nome = nome;
        this.saldo = saldoInicial;
    }

    public void depositar(double valor) {
        this.saldo = this.saldo + valor;
        System.out.printf("[ %s ] Recebeu um depósito de R$ %.2f (Saldo atual: %.2f)\n", this.nome, valor, this.saldo);
    }

    public void imprimir() {
        System.out.println("-------------------");
        System.out.printf("Cliente:   %s\n", this.nome);
        System.out.printf("Saldo:     R$%.2f\n", this.saldo);
        System.out.println("-------------------");
    }

    public void sacar(double valor) {
        if (this.saldo <= 0.0) {
            System.out.printf("[ %s ] Tentou sacar %.2f (saldo atual: %.2f)\n", this.nome, valor, this.saldo);
            return;
        }

        if ((this.saldo - valor) >= 0.0) {
            System.out.printf("[ %s ] Sacou %.2f (saldo atual: %.2f)\n", this.nome, valor, this.saldo);
            this.saldo = this.saldo - valor;

        } else {
            System.out.printf("[ %s ] Tentou sacar %.2f (saldo atual: %.2f)\n", this.nome, valor, this.saldo);
            return;
        }
    }

    public double getSaldo() {
        return this.saldo;
    }

    public String getNome() {
        return this.nome;
    }
}
