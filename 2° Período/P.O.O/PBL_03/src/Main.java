public class Main {
    public static void main(String[] args) {

        Banco bb = new Banco("Banco do Brasil");
        Cliente c1 = new Cliente("Pedro", 300.1f);
        Cliente c2 = new Cliente("Steve", 100.0f);

        bb.transferir(c1, c2, 50);

        c1.imprimir();
        c2.imprimir();
    }
}
