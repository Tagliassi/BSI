public class ImovelNovo extends Imovel {

    public ImovelNovo(String nome, Double preco){
        super(nome, preco);
    }

    public Double getAcrescimo(){
        return preco;

    }

    public String toString() {
        return "ImovelNovo []";
    }

}
