public class App {
    public static void main(String[] args) throws Exception {
      Pai pai = new Pai("Uno", 2000, "Visa", true);

      Filho filho = new Filho("Uno", 2000, "Visa", true, "Santa Maria", "PS5", true, 16);
      filho.imprimeAtributos();
      System.out.println(filho.videogame);
    }
}
