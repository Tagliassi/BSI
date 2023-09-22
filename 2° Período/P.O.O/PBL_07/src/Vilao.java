public abstract class Vilao extends Personagem {

    public Vilao() {
        this.posicao_x = 0;
        this.posicao_y = 0;
        this.posicao_z = 0;
    }

    @Override
    public void correr(float x, float y){
        this.posicao_x = x;
        this.posicao_y = y;

        String mensagem = String.format("%s Está correndo!",  toString());
        System.out.println(mensagem);
    }
}
