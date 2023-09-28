import java.util.List;

public interface Pedido {
  abstract void addProduto(Produto p);
  abstract List<Produto> getProdutos();
  abstract double calculaValorTotal();
}
