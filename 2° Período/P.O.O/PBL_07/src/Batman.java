public class Batman extends Heroi implements Camuflagem{

    public void camuflar(int cor){
        this.cor = cor;

        String mensagem = String.format("%s Está Camuflado!",  toString());
        System.out.println(mensagem);
    }

    @Override
    public void atirar() {
        String mensagem = String.format("%s Está Atirando!",  toString());
        System.out.println(mensagem);
    }    
}
