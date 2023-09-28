public abstract class Figura {
  protected String sep = " / ";
  protected double x;
  protected double y;
  protected int cor;

  Figura(double x, double y, int cor) {
    this.x = x;
    this.y = y;
    this.cor = cor;
  }

  public void deslocar(double x, double y) {
    apagar();
    this.x = x;
    this.y = y;
    desenhar();
  }

  public void colorir(int cor) {
    apagar();
    this.cor = cor;
    desenhar();
  }

  public abstract void apagar();
  public abstract void desenhar();  
}
