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
    var passwordInputs1 = document.querySelectorAll('#id_password'); 

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
});