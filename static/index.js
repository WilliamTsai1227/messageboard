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
            const textDiv = document.createElement('div');
            const img = document.createElement('img');
            const hr = document.createElement('hr');
            textDiv.textContent = result.content;  // Add text content to div
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

async function getData(){
    try{
        const response = await fetch("http://44.226.179.122/api/getdata/",{
            method:'GET'
        });
        const result = await response.json();

        if(response.status == 200 && result.success === true){
            let allMessage = result.data;
            if ( allMessage.lengh !== 0 ){   //data is not empty
                for(let i of allMessage){
                    const message_container = document.querySelector(".message_container")
                    const textDiv = document.createElement('div');
                    const img = document.createElement('img');
                    const hr = document.createElement('hr');
                    textDiv.textContent = i.content;
                    img.src = i.img_url
                    message_container.appendChild(textDiv);
                    message_container.appendChild(img);
                    message_container.appendChild(hr);
                }
            }
        }else if(response.status == 500){
            console.error("拿取既有留言板資料發生錯誤")
        }

    }catch(error){
        alert('網路錯誤，請稍後再嘗試。');
        console.error('Error:', error);
    }
}
