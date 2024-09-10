document.addEventListener('DOMContentLoaded', function() {
    // Função para a busca simulada
    const searchInput = document.querySelector('.search input');
    const searchButton = document.querySelector('.search button');

    searchButton.addEventListener('click', function() {
        const query = searchInput.value.trim();

        if (query === '') {
            alert('Digite algo para buscar.');
        } else {
            alert(`Resultados da busca por: ${query}`);
            
            searchInput.value = '';
        }
    });
}); 

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