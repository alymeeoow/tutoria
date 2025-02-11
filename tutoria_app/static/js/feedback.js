document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("feedback-modal");
    const openModalBtn = document.querySelector(".feedback-btn");
    const closeModalBtn = document.getElementById("cancel-feedback");
    const submitBtn = document.getElementById("submit-feedback");
    const stars = document.querySelectorAll(".star");

    let selectedRating = 0;

    openModalBtn.addEventListener("click", () => {
        modal.style.display = "flex";
    });

    closeModalBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });


    stars.forEach((star, index) => {
        star.addEventListener("mouseover", () => {
            
            stars.forEach((s, i) => {
                if (i <= index) {
                    s.style.color = 'gold'; 
                } else {
                    s.style.color = '#ddd';  
                }
            });
        });

        
        star.addEventListener("mouseout", () => {
            if (selectedRating === 0) {
           
                stars.forEach((s) => {
                    s.style.color = '#ddd';
                });
            } else {
             
                stars.forEach((s, i) => {
                    s.style.color = (i < selectedRating) ? 'gold' : '#ddd';
                });
            }
        });


        star.addEventListener("click", () => {
            selectedRating = index + 1; 
        
            stars.forEach((s, i) => {
                if (i < selectedRating) {
                    s.classList.add("selected");
                } else {
                    s.classList.remove("selected");
                }
            });
        });
    });

    submitBtn.addEventListener("click", () => {
        const comment = document.getElementById("feedback-comment").value;

        if (selectedRating === 0) {
            alert("Please select a rating.");
            return;
        }

        if (comment.trim() === "") {
            alert("Please provide a comment.");
            return;
        }

        alert(`Feedback Submitted!\nRating: ${selectedRating} stars\nComment: ${comment}`);
        modal.style.display = "none"; 
    });

    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
