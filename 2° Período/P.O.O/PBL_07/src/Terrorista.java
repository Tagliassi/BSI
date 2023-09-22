public abstract class Terrorista extends Vilao{
    public void atirar(){
        String mensagem = String.format("%s Está atirando!",  toString());
        System.out.println(mensagem);
    }
}