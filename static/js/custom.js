(function() {
    'use strict';

    var elToggle = document.querySelector('.js-password-show-toggle'),
        passwordInput = document.getElementById('password');

    elToggle.addEventListener('click', (e) => {
        e.preventDefault();

        if (elToggle.classList.contains('active')) {
            passwordInput.setAttribute('type', 'password');
            elToggle.classList.remove('active');
        } else {
            passwordInput.setAttribute('type', 'text');
            elToggle.classList.add('active');
        }
    });
})();

document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.getElementById('signupForm');
    const loginForm = document.getElementById('loginForm');

    if (signupForm) {
        signupForm.addEventListener('submit', function(event) {
            handleSignupSubmit(event);
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            handleLoginSubmit(event);
        });
    }
});

function handleSignupSubmit(event) {
    event.preventDefault();
    const formData = {
        //id: 0, // Ajusta según sea necesario
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        name: document.getElementById('name').value,
        password: document.getElementById('password').value
    };
    // Enviar los datos como JSON
    fetch('http://127.0.0.1:8000/users/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (response.ok) {
            return response.json(); 
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log(data);
        alert('Usuario creado con éxito');
        // Aquí rediriges a Angular con el token si lo necesitas
        //window.location.href = `http://localhost:4200/home?token=${data.access_token}`;
    })
    .catch(error => console.error('Error:', error));
}

function handleLoginSubmit(event) {
    event.preventDefault();
    const formData = {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value
    };
    // Enviar los datos como JSON
    fetch('http://127.0.0.1:8000/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (response.ok) {
            return response.json(); 
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log(data);
        // Aquí rediriges a Angular con el token si lo necesitas
        window.location.href = `http://localhost:4200/inicio?token=${data.token}`;
    })
    .catch(error => console.error('Error:', error));
}