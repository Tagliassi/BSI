public class Filho extends Pai {
  public String escola;
  public String videogame;
  
  private boolean lolzeiro;
  private int idade;

  

  public Filho(String carro, int dinheiro, String cartaoDeCredito, boolean calvice, String escola, String videogame,
      boolean lolzeiro, int idade) {
    super(carro, dinheiro, cartaoDeCredito, calvice);
    this.escola = escola;
    this.videogame = videogame;
    this.lolzeiro = lolzeiro;
    this.idade = idade;
  }  
}
