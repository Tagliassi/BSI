public class Pinguim extends Ladrao {

    @Override
    public void atirar() {
        String mensagem = String.format("%s Está atirando!",  toString());
        System.out.println(mensagem);
    }

}
