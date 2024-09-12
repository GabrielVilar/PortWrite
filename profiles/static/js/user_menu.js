document.getElementById("change-profile-pic-link").addEventListener("click", function(event) {
    var content = document.getElementById('includes');
    event.preventDefault();
    document.getElementById("profile-picture-change-container").style.display = "block";
    content.style.display = "none";
});

document.getElementById("cancel-btn").addEventListener("click", function(event) {
    var content = document.getElementById('includes');
    event.preventDefault();
    document.getElementById("profile-picture-change-container").style.display = "none";
    content.style.display = "block";
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

document.addEventListener("DOMContentLoaded", function() {
    var saveChangesBtn = document.getElementById('saveChangesBtn');
    var inputs = document.querySelectorAll('input');

    // Check if any input field is modified
    inputs.forEach(function(input) {
        input.addEventListener('input', function() {
            // Show the button if the input field value is changed
            if (input.value !== input.defaultValue) {
                saveChangesBtn.style.display = 'block';
            } else {
                // Hide the button if no changes are made in all inputs
                var anyModified = Array.from(inputs).some(function(input) {
                    return input.value !== input.defaultValue;
                });
                if (!anyModified) {
                    saveChangesBtn.style.display = 'none';
                }
            }
        });
    });
});


