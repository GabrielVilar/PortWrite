document.getElementById("change-profile-pic-link").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("profile-picture-change-container").style.display = "block";
});

document.getElementById("cancel-btn").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("profile-picture-change-container").style.display = "none";
});