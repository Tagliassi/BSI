import java.util.ArrayList;
import java.util.List;

public class PedidoJogo implements Pedido {
  private List<Produto> produtos = new ArrayList<>();

  @Override
  public void addProduto(Produto p) {
    produtos.add(p);
  }

  @Override
  public List<Produto> getProdutos() {
    return produtos;
  }

  @Override
  public double calculaValorTotal() {
    double valorTotal = 0f;
    for (Produto produto:produtos) {
      valorTotal += produto.valor;
    }
    return valorTotal;
  }
}
