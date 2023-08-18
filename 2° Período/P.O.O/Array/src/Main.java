import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<Filme> filmes = new ArrayList<Filme>();

        filmes.add(new Filme("A fuga", (short) 2018));
        filmes.add(new Filme("A chegada", (short) 2022));
        filmes.add(new Filme("A saída", (short) 2005));
        filmes.add(new Filme("A depressão", (short) 2010));
        filmes.add(new Filme("O poço", (short) 2012));

        for (int i = 0; i < filmes.size(); i++) {
            System.out.println(filmes.get(i));
        }
    }
}
