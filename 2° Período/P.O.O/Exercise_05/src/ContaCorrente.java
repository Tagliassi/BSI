public class ContaCorrente extends Conta{

    private Double taxaManutencao;

    public ContaCorrente(String nomeTitular, String numeroConta, Double taxeManutencao){
        super(nomeTitular, numeroConta);
        this.taxaManutencao = taxeManutencao;
    }
    
    public Boolean debitarManutenao(Double valor){
        if (this.saldo>0){
            this.taxaManutencao -= valor;
        }
        return false;
    }
  
}
