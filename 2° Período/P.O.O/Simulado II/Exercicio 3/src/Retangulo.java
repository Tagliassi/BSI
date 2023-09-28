public class Retangulo extends Figura {
  private double base;
  private double altura;

  public Retangulo(double x, double y, int cor, double base, double altura) {
    super(x, y, cor);
    this.base = base;
    this.altura = altura;
    desenhar();
  }

  public void apagar() {
    System.out.println("Apagando retangulo : " + x + sep + y + sep + cor + sep + base + sep +altura);
  }

  public void desenhar() {
    System.out.println("Desenhando retangulo : " + x + sep + y + sep + cor + sep + base + sep +altura);
  }
  
}
