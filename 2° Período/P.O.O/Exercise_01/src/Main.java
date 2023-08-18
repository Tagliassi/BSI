public class Main {
    public static void main(String[] args){

        ContaBanco p1 = new ContaBanco();
        p1.setNumConta(1111);
        p1.setDono("Roberto");
        p1.abrirConta("CC");
        p1.depositar(100.00);

        ContaBanco p2 = new ContaBanco();
        p2.setNumConta(2222);
        p2.setDono("Lara");
        p2.abrirConta("CP");
        p2.depositar(500.00);
        p2.sacar(100.00);

        p1.statusAtual();
        p2.statusAtual();
        
    }
}
