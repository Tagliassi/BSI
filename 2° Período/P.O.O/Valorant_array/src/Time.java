import java.util.ArrayList;
import java.util.Scanner;
public class Time {
    private ArrayList<Agentes> agentes;
    private String nome;
    private int posicao;

    public Time(String nome) {
        this.nome = nome;
        agentes = new ArrayList<Agentes>();
    }

    public String getNome(){
        return nome;
    }
    public void criarTime() {
        Scanner sc = new Scanner(System.in);

        while (agentes.size() < 5) {
            System.out.println("Digite o nome do personagem: ");
            String nomePersonagem = sc.nextLine();

            agentes.add(new Agentes(nomePersonagem));
        }
    }
    public void imprimirAgentes() {
        System.out.println("Agentes no time " + nome + ":");
        for (Agentes agente : agentes) {
            System.out.println("Nome: " + agente.getNome());
        }
    }

}
