document.addEventListener('DOMContentLoaded', function() {
    // Função para animar o clique nos botões "Learn more"
    const learnMoreButtons = document.querySelectorAll('.article-card button');

    learnMoreButtons.forEach(button => {
        button.addEventListener('click', function() {
            button.textContent = 'Loading...';
            button.disabled = true;

            // Simula um carregamento antes de redirecionar ou mostrar conteúdo
            setTimeout(() => {
                alert('colocar link learn more');
                button.textContent = 'Learn more';
                button.disabled = false;
            }, 1000);
        });
    });

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
document.addEventListener('DOMContentLoaded', function() {
    const imagePlaceholders = document.querySelectorAll('.image-placeholder img');

    imagePlaceholders.forEach(image => {
        image.addEventListener('mouseover', function() {
            image.style.transform = 'scale(1.1)';
            image.style.transition = 'transform 0.3s ease';
        });

        image.addEventListener('mouseout', function() {
            image.style.transform = 'scale(1)';
        });
    });
});


