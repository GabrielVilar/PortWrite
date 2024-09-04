document.getElementById("change-profile-pic-link").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("profile-picture-change-container").style.display = "block";
});

document.getElementById("cancel-btn").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("profile-picture-change-container").style.display = "none";
});

// JavaScript to handle image preview
document.getElementById('file-input').addEventListener('change', function(event) {
    const fileInput = event.target;
    const file = fileInput.files[0];
    const preview = document.getElementById('profile-picture-preview');
    
    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            // Update the src attribute of the img tag to show the preview
            preview.src = e.target.result;
        }

        reader.readAsDataURL(file); // Read the file as a data URL
    } else {
        // Reset to default image if no file is selected
        preview.src = "{% static 'images/default_profile.png' %}";
    }
});