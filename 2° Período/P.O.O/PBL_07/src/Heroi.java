public abstract class Heroi extends Personagem {

    public Heroi() {
        this.posicao_x = 0;
        this.posicao_y = 0;
        this.posicao_z = 0;
    }

    public void correr(float x, float y){
        this.posicao_x = x;
        this.posicao_y = y;

        String mensagem = String.format("%s Está correndo!",  toString());
        System.out.println(mensagem);
    }

    public void saltar(float z){
        this.posicao_z = z;

        String mensagem = String.format("%s Está saltando!",  toString());
        System.out.println(mensagem);
    }
}
