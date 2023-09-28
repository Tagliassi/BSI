public class App {
    public static void main(String[] args) throws Exception {
        Produto p = new Produto(10);
        Produto p1 = new Produto(20);
        Produto p2 = new Produto(30);
        Produto p3 = new Produto(40);
        Produto p5 = new Produto(50);

        PedidoJogo pj = new PedidoJogo();
        pj.addProduto(p);
        pj.addProduto(p1);
        pj.addProduto(p2);
        pj.addProduto(p3);
        pj.addProduto(p5);

        System.out.println(pj.getProdutos());
        System.out.println(pj.calculaValorTotal());
    }
}
