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
    // Password form button logic
    var saveChangesBtn = document.getElementById('saveChangesBtn');
    var passwordFormContainer = document.querySelector('.form-writer-container');
    var passwordInputs = passwordFormContainer.querySelectorAll('input');

    passwordInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            if (input.value !== input.defaultValue) {
                saveChangesBtn.style.display = 'block';
            } else {
                var anyModified = Array.from(passwordInputs).some(function(input) {
                    return input.value !== input.defaultValue;
                });
                if (!anyModified) {
                    saveChangesBtn.style.display = 'none';
                }
            }
        });
    });

    // Notifications form button logic
    var saveNotificationsBtn = document.getElementById('saveNotificationsChanges');
    var notificationsFormContainer = document.querySelector('.form-container-fields');
    var notificationInputs = notificationsFormContainer.querySelectorAll('input');

    notificationInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            if (input.value !== input.defaultValue) {
                saveNotificationsBtn.style.display = 'block';
            } else {
                var anyModified = Array.from(notificationInputs).some(function(input) {
                    return input.value !== input.defaultValue;
                });
                if (!anyModified) {
                    saveNotificationsBtn.style.display = 'none';
                }
            }
        });
    });

    // Notifications form button logic
    var saveChangesBtnUser = document.getElementById('saveChangesBtn');
    var saveChangesBtnUserContainer = document.querySelector('.form-container-fields');
    var userInputs = saveChangesBtnUserContainer.querySelectorAll('input');

    userInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            if (input.value !== input.defaultValue) {
                saveChangesBtnUser.style.display = 'block';
            } else {
                var anyModified = Array.from(userInputs).some(function(input) {
                    return input.value !== input.defaultValue;
                });
                if (!anyModified) {
                    saveChangesBtnUser.style.display = 'none';
                }
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var saveChangesBtn = document.getElementById('saveChangesBtn');
    // Select inputs only inside the 'form-writer-container' div
    var formContainer = document.querySelector('.form-writer-container');
    var inputs = formContainer.querySelectorAll('input');

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

document.addEventListener("DOMContentLoaded", function() {
    var saveChangesBtn = document.getElementById('saveChangesBtnWriter');
    // Select inputs only inside the 'form-container-fields' div
    var formContainer = document.querySelector('.form-writer-container');
    var inputs = formContainer.querySelectorAll('textarea');

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

document.addEventListener("DOMContentLoaded", function() {
    var saveChangesBtn = document.getElementById('saveChangesBtnWriter');
    // Select inputs only inside the 'form-container-fields' div
    var formContainer = document.querySelector('.form-writer-container');
    var inputs = formContainer.querySelectorAll('input');

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

document.addEventListener("DOMContentLoaded", function() {
    var charCount = document.getElementById('charCount');
    // Select inputs only inside the 'form-container-fields' div
    var formContainer = document.querySelector('.form-writer-container');
    var inputs = formContainer.querySelectorAll('textarea');

    // Check if any input field is modified
    inputs.forEach(function(input) {
        input.addEventListener('input', function() {
            // Show the button if the input field value is changed
            if (input.value !== input.defaultValue) {
                charCount.style.display = 'block';
            } else {
                // Hide the button if no changes are made in all inputs
                var anyModified = Array.from(inputs).some(function(input) {
                    return input.value !== input.defaultValue;
                });
                if (!anyModified) {
                    charCount.style.display = 'none';
                }
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var addSocialMediaBtn = document.getElementById('addSocialMediaBtn');
    var socialMediaModal = document.getElementById('socialMediaModal');
    var closeModalBtn = document.querySelector('.modal .close');
    var addSocialMediaFieldBtn = document.getElementById('addSocialMediaFieldBtn');
    var socialMediaSelect = document.getElementById('socialMediaSelect');

    // Function to open the modal
    addSocialMediaBtn.onclick = function () {
        socialMediaModal.style.display = 'block';
    };

    // Function to close the modal
    closeModalBtn.onclick = function () {
        socialMediaModal.style.display = 'none';
    };

    // Close modal if user clicks outside of it
    window.onclick = function (event) {
        if (event.target == socialMediaModal) {
            socialMediaModal.style.display = 'none';
        }
    };

    // Add selected social media field when clicking "Adicionar"
    addSocialMediaFieldBtn.onclick = function () {
        var selectedPlatform = socialMediaSelect.value.toLowerCase();
        var selectedField = document.querySelector(`.social-media-field label[for='id_${selectedPlatform}']`).parentNode;

        if (selectedField) {
            // Show the corresponding social media field (set display to block)
            selectedField.style.display = 'block';

            // Remove the selected option from the modal dropdown
            var optionToRemove = socialMediaSelect.querySelector(`option[value='${selectedPlatform}']`);
            if (optionToRemove) {
                optionToRemove.remove();
            }

            // Hide "Adicionar Rede Social" button if no more options available
            if (socialMediaSelect.options.length === 0) {
                addSocialMediaBtn.style.display = 'none';  // Hide the button
            }
        } else {
            alert('Error: Could not find the selected field.');
        }

        // Close the modal after adding the social media link field
        socialMediaModal.style.display = 'none';
    };

    // Remove social media field and add the option back to the modal
    document.querySelectorAll('.remove-social-media-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var platform = btn.dataset.platform;
            var socialMediaField = document.querySelector(`.social-media-field label[for='id_${platform}']`).parentNode;

            if (socialMediaField) {
                // Hide the social media field
                socialMediaField.style.display = 'none';

                // Add the option back to the modal
                var newOption = document.createElement('option');
                newOption.value = platform;
                newOption.text = platform.charAt(0).toUpperCase() + platform.slice(1);
                socialMediaSelect.appendChild(newOption);

                // Show the "Adicionar Rede Social" button if hidden
                addSocialMediaBtn.style.display = 'block';
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
   
    var charCountElement = document.getElementById('charCount');
    const biographyTextarea = document.getElementById('id_biography');
    const maxChars = 2036;

    // Add an event listener to track input in biography
    biographyTextarea.addEventListener('input', function() {
        const currentLength = biographyTextarea.value.length;
        charCountElement.textContent = `${currentLength} / ${maxChars}`;
    });
});

document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', function () {
        const target = document.getElementById(this.getAttribute('data-target'));
        const type = target.getAttribute('type') === 'password' ? 'text' : 'password';
        target.setAttribute('type', type);
        this.textContent = type === 'password' ? '👁️' : '🙈';
    });
});
