function validarFormulario() {
    // Recupera os valores dos inputs
    var nome = document.getElementById("nome").value;
    var email = document.getElementById("email").value;
    var telefone = document.getElementById("telefone").value;
    var senha = document.getElementById("senha").value;
    var confirmarSenha = document.getElementById("confirmar_senha").value;

    // Validação básica
    if (nome === "") {
        alert("Por favor, digite seu nome completo.");
        return;
    }

    if (email === "") {
        alert("Por favor, digite seu email.");
        return;
    }

    if (email === "") {
        alert("Por favor, digite um email válido.");
        return;
    }

    if (telefone === "") {
        alert("Por favor, digite seu telefone.");
        return;
    } else if (telefone.length < 9) {
        alert("Telefone inválido, digite um telefone válido!");
        return;
    }

    if (senha === "") {
        alert("Por favor, digite sua senha.");
        return;
    }

    if (confirmarSenha === "") {
        alert("Por favor, confirme sua senha.");
        return;
    }

    if (senha !== confirmarSenha) {
        alert("As senhas não coincidem.");
        return;
    }

    // Se chegou até aqui, todos os campos são válidos
    alert("Formulário enviado com sucesso!");

}