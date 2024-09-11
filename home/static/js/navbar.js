function toggleMenu(event) {
    event.preventDefault(); 
    const dropdownMenu = document.getElementById('dropdown-menu');

    if (dropdownMenu.style.display === 'none' || dropdownMenu.style.display === '') {
        dropdownMenu.style.display = 'block';
    } else {
        dropdownMenu.style.display = 'none';
    }
}
document.addEventListener('click', function(event) {
    const dropdownMenu = document.getElementById('dropdown-menu');
    const profileLink = document.getElementById('profile-pic-link');

    if (!profileLink.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.style.display = 'none';
    }
});