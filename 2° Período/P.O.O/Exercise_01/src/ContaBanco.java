public class ContaBanco {

    public int numConta;
    protected String tipo;
    private String dono;
    private double saldo;
    private boolean status;

    public void statusAtual(){
        System.out.println();
        System.out.println("Conta:"+ this.getNumConta());
        System.out.println("Tipo:"+ this.getTipo());
        System.out.println("Dono:"+ this.getDono());
        System.out.println("Saldo:"+ this.getSaldo());
        System.out.println("Status da conta:"+ this.isStatus());
    }

    public void abrirConta(String tipo) {
        this.setTipo(tipo);
        this.setStatus(true);
        if (tipo == "CC") {
            this.setSaldo(50.0f);
        } else if (tipo == "CP") {
            this.setSaldo(150.0f);
        } else
            System.out.println("ERRO! Escolha (CC) para conta corrente ou (CP) para conta poupança!");
    }

    public void fecharConta() {
        if(this.getSaldo() > 0){
            System.out.println("A sua conta possuí dinheiro");
        }
        else if(this.getSaldo() < 0){
            System.out.println("A sua conta está em débito");
        }
        else{this.setStatus(false);}
    }

    public void depositar(double valor) {
        if(this.isStatus() == true){
            this.setSaldo(this.getSaldo() + valor);
        }
        else {System.out.println("Conta fechada, impossível depositar!");}
    }

    public void sacar(double valor) {
        if(this.isStatus() == true){
            if(this.getSaldo() >= valor) {
                this.setSaldo(this.getSaldo() - valor);
            }
            else {System.out.println("Saldo insuficiente");}
        }
        else {System.out.println("Conta fechada, impossível sacar!");}
    }

    public void pagarMensal() {
        double taxa = 0;
        if(this.getTipo() == "CC"){
            taxa = 12;
        }
        else {taxa = 20;}
        if(this.isStatus() == true){
            if(this.getSaldo() >= taxa) {
                this.setSaldo(this.getSaldo() - taxa);
            }
            else {System.out.println("Saldo insuficiente");}
        }
        else {System.out.println("Conta fechada, impossível pagar mensalidade!");}
    }

    public ContaBanco() {
        this.saldo = 0;
        this.status = false;
    }

    public String getDono() {
        return dono;
    }

    public int getNumConta() {
        return numConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public String getTipo() {
        return tipo;
    }

    public boolean isStatus() {
        return status;
    }

    public void setDono(String dono) {
        this.dono = dono;
    }

    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

}
