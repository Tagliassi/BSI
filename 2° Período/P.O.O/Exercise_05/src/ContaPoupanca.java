public class ContaPoupanca extends Conta {

    private Double taxaRendimento;

    public ContaPoupanca(String nomeTitular, String numeroConta, Double taxaRendimento){
        super(nomeTitular, numeroConta);
        this.taxaRendimento = taxaRendimento;
    }
    
    public Boolean debitarRendimento(){
        return super.depositar(taxaRendimento);
    }

}
