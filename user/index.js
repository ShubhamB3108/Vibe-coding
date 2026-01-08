const cards = document.getElementById("cards");
const title = document.getElementById("title");
const modal = document.getElementById("modal");
const availableBtn = document.getElementById("availableBtn");
const bookedBtn = document.getElementById("bookedBtn");

function renderAvailable() {
    title.innerText = "Available Meals";
    cards.innerHTML = "";

    ["Breakfast","Lunch","Dinner","Snacks"].forEach(meal => {
        cards.innerHTML += `
        <div class="card">
            <h2>${meal}</h2>
            <div class="info">
                <div class="info-item">
                    <label>Uploaded date</label>
                    <div class="pill">15/3/2026</div>
                </div>
                <div class="info-item">
                    <label>Poll closing time</label>
                    <div class="pill">3:00 PM</div>
                </div>
            </div>
            <button onclick="openModal()">Book Meal</button>
        </div>`;
    });
}

function renderBooked() {
    title.innerText = "Booked Meals";
    cards.innerHTML = "";

    for(let i=0;i<4;i++){
        cards.innerHTML += `
        <div class="card">
            <h2>Breakfast</h2>
            <div class="info">
                <div class="info-item">
                    <label>Uploaded date</label>
                    <div class="pill">15/3/2026</div>
                </div>
                <div class="info-item">
                    <label>Booked Time</label>
                    <div class="pill">3:00 PM</div>
                </div>
            </div>
            <button>View Meal Details</button>
        </div>`;
    }
}

function openModal() {
    modal.classList.add("active");
}

function closeModal() {
    modal.classList.remove("active");
}

/* Toggle */
availableBtn.onclick = () => {
    availableBtn.classList.add("active");
    bookedBtn.classList.remove("active");
    renderAvailable();
};

bookedBtn.onclick = () => {
    bookedBtn.classList.add("active");
    availableBtn.classList.remove("active");
    renderBooked();
};

/* Checkbox */
document.addEventListener("click", e => {
    if(e.target.classList.contains("check")){
        e.target.classList.toggle("active");
    }
});

/* Quantity */
document.addEventListener("click", e => {
    if(e.target.innerText === "+"){
        e.target.previousElementSibling.innerText++;
    }
    if(e.target.innerText === "-"){
        let span = e.target.nextElementSibling;
        if(span.innerText > 1) span.innerText--;
    }
});

renderAvailable();
/* CHECKBOX TOGGLE */
document.addEventListener("click", e => {
    if(e.target.classList.contains("check")){
        e.target.classList.toggle("active");

        const row = e.target.closest(".row");
        const text = row.querySelector("span");

        if(e.target.classList.contains("active")){
            text.classList.remove("strike");
        } else {
            text.classList.add("strike");
        }
    }
});

/* QUANTITY CONTROL */
document.addEventListener("click", e => {
    if(e.target.innerText === "+"){
        e.target.previousElementSibling.innerText++;
    }

    if(e.target.innerText === "-"){
        const span = e.target.nextElementSibling;
        if(span.innerText > 1){
            span.innerText--;
        }
    }
});

/* Checkbox strike toggle */
document.querySelectorAll(".custom-checkbox input").forEach(cb => {
    cb.addEventListener("change", () => {
        const text = cb.parentElement.querySelector(".label-text");
        text.classList.toggle("strike", !cb.checked);
    });
});
