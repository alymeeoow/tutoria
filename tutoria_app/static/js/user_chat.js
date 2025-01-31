function triggerFileUpload() {
    document.getElementById('upload-image').click();
  }
  
  
  document.getElementById('photoBtn').addEventListener('click', function () {
    document.getElementById('popupModal').style.display = 'flex';
  });
  
  document.getElementById('popupModal').addEventListener('click', function (event) {
    if (event.target === this) {
      this.style.display = 'none'; 
    }
  });
  
  
  document.getElementById('cameraOption').addEventListener('click', function () {
    document.getElementById('popupModal').style.display = 'none'; 
    document.getElementById('fileInput').click(); 
  });
  
  
  document.getElementById('galleryOption').addEventListener('click', function () {
    document.getElementById('popupModal').style.display = 'none'; 
    document.getElementById('uploadInput').click(); 
  });
  
  
  document.getElementById('fileInput').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        appendImageToChat(e.target.result, 'sent'); 
      };
      reader.readAsDataURL(file);
    }
  });
  
  
  document.getElementById('uploadInput').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        appendImageToChat(e.target.result, 'sent'); 
      };
      reader.readAsDataURL(file);
    }
  });
  
  
  function appendImageToChat(imageSrc, messageType) {
    const chatMessages = document.querySelector('.chat-messages');
    const messageContainer = document.createElement('div');
    messageContainer.className = `message-container ${messageType}`;
    
    const imageElement = document.createElement('img');
    imageElement.src = imageSrc;
    imageElement.alt = 'Uploaded Image';
    imageElement.style.maxWidth = '200px';
    imageElement.style.borderRadius = '10px';
  
    const avatar = document.createElement('img');
  
  
    avatar.className = 'message-avatar';
  
    if (messageType === 'sent') {
      messageContainer.appendChild(imageElement); 
      messageContainer.appendChild(avatar); 
    } else {
      messageContainer.appendChild(avatar); 
      messageContainer.appendChild(imageElement); 
    }
  
    chatMessages.appendChild(messageContainer);
    chatMessages.scrollTop = chatMessages.scrollHeight; 
  }
  