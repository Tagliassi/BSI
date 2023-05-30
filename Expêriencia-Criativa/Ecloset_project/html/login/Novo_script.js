/* 
   Este trecho de código JavaScript atribui referências aos botões de registro e login
   com base em seus respectivos ids no HTML. Além disso, obtém referência ao contêiner principal.
*/
const registerButton = document.getElementById("cadastro");
const loginButton = document.getElementById("login");
const container = document.getElementById("bloco-principal");

/* 
   Aqui, é adicionado um ouvinte de evento ao botão de registro. Quando o botão é clicado,
   a classe "right-panel-active" é adicionada ao contêiner, o que aciona a transição para o formulário de registro.
*/
registerButton.addEventListener("click", () => {
  container.classList.add("painel-direito-ativado");
});

/* 
   Da mesma forma, é adicionado um ouvinte de evento ao botão de login. Quando o botão é clicado,
   a classe "right-panel-active" é removida do contêiner, revertendo para o formulário de login.
*/
loginButton.addEventListener("click", () => {
  container.classList.remove("painel-direito-ativado");
});
