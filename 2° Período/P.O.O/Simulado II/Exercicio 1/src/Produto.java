public class Produto {
  private int codigo;
  private double peso;


  public Produto(int codigo, double peso) {
    this.codigo = codigo;
    this.peso = peso;
  }

  public double seguro() {
    return (peso * 10);
  }

}
