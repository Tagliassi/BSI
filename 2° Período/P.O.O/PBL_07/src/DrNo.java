public class DrNo extends Terrorista {
    @Override
    public void saltar(float z) {
        this.posicao_z = z;
        
        String mensagem = String.format("%s Está saltando!",  toString());
        System.out.println(mensagem);
    }
}
