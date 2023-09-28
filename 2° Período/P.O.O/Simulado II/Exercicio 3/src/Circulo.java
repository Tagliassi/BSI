public class Circulo extends Figura {
  private double raio;

  public Circulo(double x, double y, int cor, double raio) {
    super(x, y, cor);
    this.raio = raio;
    desenhar();
  }

  public void apagar() {
    System.out.println("Apagando circulo : " + x + sep + y + sep + cor + sep + raio);
  }

  public void desenhar() {
    System.out.println("Desenhando circulo : " + x + sep + y + sep + cor + sep + raio);
  }  
}
