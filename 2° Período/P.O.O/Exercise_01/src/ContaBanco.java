public class ContaBanco {

    public int numConta;
    protected String tipo;
    private String dono;
    private double saldo;
    private boolean status;

    public void abrirConta(String tipo) {
        setTipo(tipo);
        setStatus(true);
        if (tipo == "CC") {
            setSaldo(50.0f);
        } else if (tipo == "CP") {
            setSaldo(150.0f);
        } else
            System.out.println("ERRO! Escolha (CC) para conta corrente ou (CP) para conta poupança!");
    }

    public void fecharConta() {

    }

    public void depositar() {

    }

    public void sacar() {

    }

    public void pagarMensal() {

    }

    public ContaBanco() {
        double saldo = 0;
        boolean status = false;
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
