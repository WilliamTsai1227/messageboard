async function handleSubmit(event) {
    event.preventDefault();  // prevent the form submit action
    
    const formData = new FormData(event.target);  // Get form data
    
    try {
        const response = await fetch('http://44.226.179.112/api/upload/', {
            method: 'POST',
            body: formData  
        });
        
        const result = await response.json();  

        if (response.status === 200) {
            const message_container = document.querySelector(".message_container")
            const contentDiv = document.createElement('div');
            const img = document.createElement('img');
            const hr = document.createElement('hr');
            contentDiv.textContent = result.content;  // Add text content to div
            img.src = result.img_url;  // Add the source url of the image
            message_container.appendChild(contentDiv);
            message_container.appendChild(img);
            message_container.appendChild(hr);
        } else if (response.status === 500) {
            alert('上傳失敗');
        }
    } catch (error) {
        alert('網路錯誤，請稍後再嘗試。');
        console.error('Error:', error);
    }
}
