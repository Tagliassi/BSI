public class Partida {
    public static void main(String[] args) {
        Time time1 = criarTime("Time A");
        Time time2 = criarTime("Time B");

        System.out.println("Time " + time1.getNome() + " - Agentes:");
        time1.imprimirAgentes();

        System.out.println("Time " + time2.getNome() + " - Agentes:");
        time2.imprimirAgentes();
    }

    public static Time criarTime(String nome) {
        Time time = new Time(nome);
        time.criarTime();
        return time;
    }
}