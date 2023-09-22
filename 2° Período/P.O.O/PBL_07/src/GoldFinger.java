public class GoldFinger extends Terrorista implements Personificacao{

    private Heroi heroi;
    
    public void camuflar(int cor){
        this.cor = cor;

        String mensagem = String.format("%s Está camuflando!",  toString());
        System.out.println(mensagem);
    }

    public void personificar(Heroi h){
        this.heroi = h;
        String mensagem = String.format("%s Personificando!",  toString());
        System.out.println(mensagem);
    }

    @Override
    public void saltar(float z) {
        String mensagem = String.format("%s Está saltando!",  toString());
        System.out.println(mensagem);
    }

}
