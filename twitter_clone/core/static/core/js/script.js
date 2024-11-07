// script.js

// Função para validar se os campos de login estão preenchidos
function validateLoginForm() {
    const username = document.querySelector('input[name="username"]');
    const password = document.querySelector('input[name="password"]');
    if (username.value === "" || password.value === "") {
        alert("Por favor, preencha todos os campos.");
        return false;  // Impede o envio do formulário se os campos estiverem vazios
    }
    return true;
}

// Função para validar o formulário de cadastro
function validateSignupForm() {
    const username = document.querySelector('input[name="username"]');
    const email = document.querySelector('input[name="email"]');
    const password1 = document.querySelector('input[name="password1"]');
    const password2 = document.querySelector('input[name="password2"]');
    
    if (username.value === "" || email.value === "" || password1.value === "" || password2.value === "") {
        alert("Por favor, preencha todos os campos.");
        return false;
    }

    // Verifica se as senhas são iguais
    if (password1.value !== password2.value) {
        alert("As senhas não coincidem.");
        return false;
    }

    return true;
}

// Adicionando validação no envio dos formulários
document.querySelector('form').addEventListener('submit', function(e) {
    // Verificando qual formulário é
    if (e.target.action.includes("signup")) {
        if (!validateSignupForm()) {
            e.preventDefault(); // Impede o envio se não passar na validação
        }
    } else {
        if (!validateLoginForm()) {
            e.preventDefault(); // Impede o envio se não passar na validação
        }
    }
});

// Funcionalidade de mostrar/ocultar senha
document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', function() {
        const passwordField = this.previousElementSibling;  // Campo de senha anterior ao botão
        if (passwordField.type === "password") {
            passwordField.type = "text";  // Exibe a senha
            this.innerText = "Esconder senha";  // Muda o texto do botão
        } else {
            passwordField.type = "password";  // Esconde a senha
            this.innerText = "Mostrar senha";  // Muda o texto do botão
        }
    });
});
