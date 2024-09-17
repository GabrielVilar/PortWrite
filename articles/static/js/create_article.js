document.addEventListener('DOMContentLoaded', function() {
    
    const coverImageInput = document.querySelector('input[name="cover_image"]');
    const coverImageDiv = document.querySelector('.cover-img');
    
    coverImageInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                coverImageDiv.innerHTML = `<img src="${e.target.result}" alt="Cover Image" style="width:100%; height:auto;" />`;
            };
            reader.readAsDataURL(file);
        }
    });

    const imageInput = document.querySelector('input[name="images"]');
    const videoInput = document.querySelector('input[name="video"]');
    const contentArea = document.querySelector('.content-area');

    imageInput.addEventListener('change', function(event) {
        const files = event.target.files;
        Array.from(files).forEach(file => {
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const subtitle = document.querySelector('input[name="subtitle"]').value;
                    contentArea.innerHTML += `
                        <div class="article-image">
                            <img src="${e.target.result}" alt="Article Image" style="max-width:100%; height:auto;" />
                            ${subtitle ? `<p class="image-subtitle">${subtitle}</p>` : ''}
                        </div>
                    `;
                };
                reader.readAsDataURL(file);
            }
        });
    });

    videoInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                contentArea.innerHTML += `
                    <div class="article-video">
                        <video controls style="max-width:100%; height:auto;">
                            <source src="${e.target.result}" type="${file.type}">
                            Your browser does not support the video tag.
                        </video>
                    </div>
                `;
            };
            reader.readAsDataURL(file);
        }
    });

});
