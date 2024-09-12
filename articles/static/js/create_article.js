function addContent(type) {
    const contentArea = document.getElementById('contentArea');
    
    switch (type) {
        case 'image':
            const imgUrl = prompt("Insira a URL da imagem:");
            if (imgUrl) {
                contentArea.innerHTML += `<img src="${imgUrl}" alt="Imagem" style="max-width: 100%; margin: 10px 0;">`;
            }
            break;
        case 'text':
            const text = prompt("Insira o texto:");
            if (text) {
                contentArea.innerHTML += `<p>${text}</p>`;
            }
            break;
        case 'grid':
            const gridHtml = `
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
                    <img src="https://via.placeholder.com/150" alt="Foto 1">
                    <img src="https://via.placeholder.com/150" alt="Foto 2">
                    <img src="https://via.placeholder.com/150" alt="Foto 3">
                </div>`;
            contentArea.innerHTML += gridHtml;
            break;
        case 'video':
            const videoUrl = prompt("Insira a URL do vídeo/áudio:");
            if (videoUrl) {
                contentArea.innerHTML += `<video controls style="max-width: 100%; margin: 10px 0;">
                                             <source src="${videoUrl}" type="video/mp4">
                                             Seu navegador não suporta vídeo.
                                           </video>`;
            }
            break;
        case 'embed':
            const embedCode = prompt("Insira o código incorporado (embed):");
            if (embedCode) {
                contentArea.innerHTML += embedCode;
            }
            break;
        default:
            break;
    }
}

function publishArticle() {
    const content = document.getElementById('contentArea').innerHTML;
    if (content.trim()) {
        alert("Seu artigo foi publicado com sucesso!");
    } else {
        alert("O conteúdo está vazio. Adicione algo antes de publicar.");
    }
}
