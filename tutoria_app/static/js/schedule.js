document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("scheduleModal");
    const openModal = document.querySelector(".schedule-btn");
    const closeModal = document.getElementById("closeModal");
    const startDateInput = document.getElementById("startDate");
    const endDateInput = document.getElementById("endDate");

 
    let today = new Date().toISOString().split('T')[0];
    startDateInput.setAttribute("min", today);
    endDateInput.setAttribute("min", today);


    startDateInput.addEventListener("change", function () {
        endDateInput.setAttribute("min", startDateInput.value);
    });

    openModal.addEventListener("click", function () {
        modal.style.display = "flex";
        document.body.classList.add("modal-open"); 
    });

    closeModal.addEventListener("click", function () {
        modal.style.display = "none"; 
        document.body.classList.remove("modal-open"); 
    });

  
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
            document.body.classList.remove("modal-open");
        }
    });
});


function redirect() {
    window.location.href = teacherProfile2URL; 
}

function back() {
    window.location.href = teacherProfileURL; 
}







