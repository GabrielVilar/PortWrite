function toggleDropdown() {
    const dropdownMenu = document.getElementById('dropdown-menu');
    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
}
document.addEventListener('DOMContentLoaded', function() {
    // Função para animar o clique nos botões "Learn more"
    const learnMoreButtons = document.querySelectorAll('.card button');

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
    })});