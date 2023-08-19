import java.util.Random;

public class Luta {

    private Lutador desafiado;
    private Lutador desafiante;
    private int rounds;
    private boolean aprovada;

    public void marcarLuta(Lutador desafiante, Lutador desafiado){

        if(desafiante.getCategoria().equals(desafiado.getCategoria()) && desafiante != desafiado){
           this.setAprovada(true);
           this.desafiado = desafiado;
           this.desafiante = desafiante;
        }
        else{
            this.setAprovada(false);
            this.desafiado = null;
            this.desafiante = null;
        }
    }

    public void lutar(){

        if(this.isAprovada()){
            System.out.println("Desafiado");
            this.desafiado.apresentar();
            System.out.println("==========================================================");
            System.out.println("Desafiante");
            this.desafiante.apresentar();
            System.out.println("==========================================================");

            Random aleatorio = new Random();
            int vencedor = aleatorio.nextInt(3);
            

            switch (vencedor) {
                case 0:
                    System.out.println("==========================================================");
                    System.out.println("A luta empatou!");
                    this.desafiado.empatarLuta();
                    this.desafiante.empatarLuta();
                    break;
                case 1:
                    System.out.println("==========================================================");
                    System.out.println("O lutador "+this.desafiado.getNome()+ " ganhou a luta");
                    System.out.println("O lutador "+this.desafiante.getNome()+ " perdeu a luta");
                    this.desafiado.ganharLuta();
                    this.desafiante.perderLuta();
                    break;
                case 2:
                    System.out.println("==========================================================");
                    System.out.println("O lutador "+this.desafiado.getNome()+ " perdeu a luta");
                    System.out.println("O lutador "+this.desafiante.getNome()+ " ganhou a luta");
                    this.desafiante.ganharLuta();
                    this.desafiado.perderLuta();
                    break;
            }
        }
        else{System.out.println("Luta não pode acontecer!");}

    }

    public Lutador getDesafiado() {
        return desafiado;
    }

    public Lutador getDesafiante() {
        return desafiante;
    }

    public int getRounds() {
        return rounds;
    }

    public boolean isAprovada() {
        return aprovada;
    }

    public void setAprovada(boolean aprovada) {
        this.aprovada = aprovada;
    }

    public void setDesafiado(Lutador desafiado) {
        this.desafiado = desafiado;
    }

   public void setDesafiante(Lutador desafiante) {
       this.desafiante = desafiante;
   }
   
   public void setRounds(int rounds) {
       this.rounds = rounds;
   }
    
}
