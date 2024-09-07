document.getElementById('signupForm').addEventListener('submit', function(event) {
    const password = document.getElementById('id_password1').value;  // Updated to use 'id_' prefix that Django adds by default
    const confirmPassword = document.getElementById('id_password2').value;  // Updated to use 'id_' prefix that Django adds by default
    
    if (password !== confirmPassword) {
        event.preventDefault();  // Prevent form submission only if passwords do not match
        // Trigger SweetAlert
        Swal.fire({
            icon: 'error',
            title: 'As senhas não coincidem!',
            text: 'Certifique-se de que ambas as senhas são iguais.',
            confirmButtonText: 'OK',
            width: '350px'
        });
    } else {
        // Allow the form to be submitted as usual
    }
});

function togglePasswordVisibility(inputId, eyeIcon) {
    const inputField = document.getElementById(inputId);
    if (inputField.type === 'password') {
        inputField.type = 'text'; // Show password
        eyeIcon.textContent = '🙈'; // Change icon to 'hide' icon
    } else {
        inputField.type = 'password'; // Hide password
        eyeIcon.textContent = '👁️'; // Change icon to 'show' icon
    }
}

document.addEventListener("DOMContentLoaded", function() {
    var eyebutton1 = document.getElementById('pass1'); 
    var eyebutton2 = document.getElementById('pass2'); 
    var passwordInputs1 = document.querySelectorAll('#id_password1'); 
    var passwordInputs2 = document.querySelectorAll('#id_password2');

    // Check if the password fields are modified
    passwordInputs1.forEach(function(input) {
        input.addEventListener('input', function() {
            // Show the eye button if the password field value is changed
            if (input.value !== '') {
                eyebutton1.style.display = 'block';
            } else {
                // Hide the button if both password fields are empty
                var anyPasswordEntered = Array.from(passwordInputs1).some(function(input) {
                    return input.value !== '';
                });
                if (!anyPasswordEntered) {
                    eyebutton1.style.display = 'none';
                }
            }
        });
    });

    passwordInputs2.forEach(function(input) {
        input.addEventListener('input', function() {
            // Show the eye button if the password field value is changed
            if (input.value !== '') {
                eyebutton2.style.display = 'block';
            } else {
                // Hide the button if both password fields are empty
                var anyPasswordEntered = Array.from(passwordInputs2).some(function(input) {
                    return input.value !== '';
                });
                if (!anyPasswordEntered) {
                    eyebutton2.style.display = 'none';
                }
            }
        });
    });
});