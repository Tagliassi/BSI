public class ImovelNovo extends Imovel {

    public ImovelNovo(String nome, Double preco){
        super(nome, preco);
    }

    public Double getAcrescimo(Double valor){
        return valor*1.10;
    }

    public String toString() {
        return "ImovelNovo []";
    }

}
