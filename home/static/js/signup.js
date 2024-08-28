document.getElementById('signupForm').addEventListener('submit', function(event) {
    const password = document.getElementById('id_password1').value;  // Updated to use 'id_' prefix that Django adds by default
    const confirmPassword = document.getElementById('id_password2').value;  // Updated to use 'id_' prefix that Django adds by default
    
    if (password !== confirmPassword) {
        event.preventDefault();  // Prevent form submission only if passwords do not match
        alert("Passwords do not match!");
    } else {
        // Allow the form to be submitted as usual
    }
});