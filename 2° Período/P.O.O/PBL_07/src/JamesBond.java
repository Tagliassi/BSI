public class JamesBond extends Heroi{

    @Override
    public void atirar() {
        String mensagem = String.format("%s Está Atirando!",  toString());
        System.out.println(mensagem);
    }

    
}
