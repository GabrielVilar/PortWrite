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