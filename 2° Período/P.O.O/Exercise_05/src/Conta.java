public class Conta {
    protected String nomeTitular, numeroConta, dataAbertura;
    protected Double saldo;

    public Conta(String nome, String conta){
        this.nomeTitular = nome;
        this.numeroConta = conta;
    }

    public Double sacar(Double valor){
        if (saldo<valor){
            System.out.println("Sem saldo sulficiente");
            return -1.0;
        }
        return this.saldo = this.saldo - valor;
    }

    public Boolean depositar(Double valor){
        if (valor>0){
            this.saldo = this.saldo + valor;
        }
        return false;
    }

}
