public class Pai {
  public String carro;
  public int dinheiro;
  private String cartaoDeCredito;
  private boolean calvice;
  
  public Pai(String carro, int dinheiro, String cartaoDeCredito, boolean calvice) {
    this.carro = carro;
    this.dinheiro = dinheiro;
    this.cartaoDeCredito = cartaoDeCredito;
    this.calvice = calvice;
  }

  void imprimeAtributos() {
    String calvo = calvice ? "é" : "não é";
    System.out.println("Dirige um " + carro + "\nTem " + dinheiro + " reais");
    System.out.println("O cartão é " + cartaoDeCredito + " e ele " + calvo + " calvo");
  }

}
