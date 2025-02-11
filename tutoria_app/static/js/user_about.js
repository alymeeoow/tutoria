let uploadInterval; 

function startUpload() {
    const fileInput = document.getElementById('fileUpload');
    if (!fileInput.files.length) {
        return; 
    }

    const progressContainer = document.getElementById('progressContainer');
    const uploadComplete = document.getElementById('uploadComplete');
    const progressBar = document.getElementById('uploadProgress');
    const progressText = document.getElementById('progressText');
    const browseBtn = document.getElementById('browseBtn');
    const cancelButton = document.getElementById('cancelButton');


    progressBar.value = 0;
    progressText.textContent = '0%';


    browseBtn.classList.add('hidden');
    progressContainer.classList.remove('hidden');
    cancelButton.style.display = 'block';

    let progress = 0;
    uploadInterval = setInterval(() => {
        if (progress >= 100) {
            clearInterval(uploadInterval);
            progressText.textContent = '100%';
            progressContainer.classList.add('hidden');
            uploadComplete.classList.remove('hidden');
        } else {
            progress += 5;
            progressBar.value = progress;
            progressText.textContent = progress + '%';
        }
    }, 500);
}

function cancelUpload() {
    const progressContainer = document.getElementById('progressContainer');
    const browseBtn = document.getElementById('browseBtn');
    const uploadComplete = document.getElementById('uploadComplete');
    const progressBar = document.getElementById('uploadProgress');
    const progressText = document.getElementById('progressText');
    const cancelButton = document.getElementById('cancelButton');
    const fileInput = document.getElementById('fileUpload');


    clearInterval(uploadInterval);


    progressBar.value = 0;
    progressText.textContent = '0%';

 
    progressContainer.classList.add('hidden');
    uploadComplete.classList.add('hidden');
    cancelButton.style.display = 'none';

    browseBtn.classList.remove('hidden');


    fileInput.value = '';
}

function reUpload() {
    cancelUpload();
    document.getElementById('fileUpload').click();
}



function displayImage(event) {
    const uploadBox = document.querySelector('.upload-placeholder');
    const file = event.target.files[0];

    if (file) {
        const validExtensions = ['image/jpeg', 'image/jpg', 'image/png'];
        const fileExtension = file.name.split('.').pop().toLowerCase();
        
        if (!validExtensions.includes(file.type) || !['jpg', 'jpeg', 'png'].includes(fileExtension)) {
            showWarningModal("Invalid file type. Please upload a JPEG or PNG image.");
            event.target.value = ""; 
            return;
        }

        if (file.size > 5 * 1024 * 1024) {
            showWarningModal("File size exceeds 5MB limit.");
            event.target.value = ""; 
            return;
        }

        const reader = new FileReader();
        reader.onload = function (e) {
            uploadBox.innerHTML = `<img src="${e.target.result}" style="width: 100%; height: 100%; border-radius: 8px; background-color: #fff;">`;
        };
        reader.readAsDataURL(file);
    }
}

function triggerFileUpload() {
    const fileInput = document.getElementById('profileUpload');
    fileInput.value = "";
    fileInput.click();
}

function showWarningModal() {
    document.getElementById('fileTypeModal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('fileTypeModal').style.display = 'none';
}
