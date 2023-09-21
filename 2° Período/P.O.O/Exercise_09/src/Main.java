public class Main {
    public static void main(String[] args) throws Exception {

        Compactado compactado = new Compactado();

        compactado.adicionaArquivo(new Texto());
        compactado.adicionaArquivo(new Imagem());
        compactado.adicionaArquivo(new Video());
        compactado.adicionaArquivo(new Planilha());
        compactado.adicionaArquivo(new Apresentacao());
        
    }
}
