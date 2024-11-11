function validateLoginForm() {
    const username = document.querySelector('input[name="username"]');
    const password = document.querySelector('input[name="password"]');
    if (username.value === "" || password.value === "") {
        alert("Por favor, preencha todos os campos.");
        return false;
    }
    return true;
}

function validateSignupForm() {
    const username = document.querySelector('input[name="username"]');
    const email = document.querySelector('input[name="email"]');
    const password1 = document.querySelector('input[name="password1"]');
    const password2 = document.querySelector('input[name="password2"]');
    
    if (username.value === "" || email.value === "" || password1.value === "" || password2.value === "") {
        alert("Por favor, preencha todos os campos.");
        return false;
    }

    if (password1.value !== password2.value) {
        alert("As senhas não coincidem.");
        return false;
    }

    return true;
}

document.querySelector('form').addEventListener('submit', function(e) {
    if (e.target.action.includes("signup")) {
        if (!validateSignupForm()) {
            e.preventDefault(); 
        }
    } else {
        if (!validateLoginForm()) {
            e.preventDefault();
        }
    }
});
