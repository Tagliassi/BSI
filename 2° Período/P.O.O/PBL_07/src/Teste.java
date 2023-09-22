public class Teste {
    public static void main(String[] args) throws Exception {

    Batman robert = new Batman();
    JamesBond daniel = new JamesBond();
    Coringa joker = new Coringa();
    Pinguim pingo = new Pinguim();
    GoldFinger dedoDourado = new GoldFinger();
    DrNo vilaoEstranho = new DrNo();

    robert.atirar();
    robert.camuflar(2);

    daniel.atirar();
    daniel.saltar(3);

    joker.atirar();

    pingo.atirar();
    pingo.correr(1, 1);

    dedoDourado.saltar(2);
    dedoDourado.camuflar(2);
    dedoDourado.personificar(daniel);

    vilaoEstranho.saltar(1);
    vilaoEstranho.atirar();
    vilaoEstranho.correr(2, 2);
        
    }
}
