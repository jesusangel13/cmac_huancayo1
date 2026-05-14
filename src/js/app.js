// app.js

const card = document.querySelector(".card");

document.addEventListener("mousemove", (e) => {

    const x = e.clientX;
    const y = e.clientY;

    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    const rotateX = (y - centerY) / 40;
    const rotateY = (centerX - x) / 40;

    if(card){

        card.style.transform =
        `
        rotateX(${rotateX}deg)
        rotateY(${rotateY}deg)
        `;
    }

});


const inputs = document.querySelectorAll("input");

inputs.forEach((input) => {

    input.addEventListener("focus", () => {

        input.style.boxShadow =
        "0 0 20px rgba(255,0,0,0.8)";

    });

    input.addEventListener("blur", () => {

        input.style.boxShadow = "none";

    });

});


function createParticle(){

    const particle =
    document.createElement("div");

    particle.classList.add("particle");

    document.body.appendChild(particle);

    particle.style.left =
    Math.random() * window.innerWidth + "px";

    particle.style.animationDuration =
    Math.random() * 3 + 2 + "s";

    particle.style.opacity =
    Math.random();

    const size =
    Math.random() * 8 + 4;

    particle.style.width =
    size + "px";

    particle.style.height =
    size + "px";

    setTimeout(() => {

        particle.remove();

    }, 5000);

}

setInterval(createParticle, 120);


const forms =
document.querySelectorAll("form");

const loadingScreen =
document.getElementById("loadingScreen");

forms.forEach((form) => {

    form.addEventListener("submit", () => {

        loadingScreen.style.display = "flex";

    });

});