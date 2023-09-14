public class ImovelVelho extends Imovel{

    public ImovelVelho(String nome, Double preco){
        super(nome, preco);
    }

    public Double getDesconto(Double valor){
        return valor*0.90;
    }

    public String toString() {
        return "ImovelVelho []";
    }
   
}
