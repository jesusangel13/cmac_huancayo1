// =========================
// LOGIN FORM
// =========================

const form =
document.getElementById(
    "loginForm"
);


// =========================
// LOADING
// =========================

const loadingScreen =
document.getElementById(
    "loadingScreen"
);

const loadingVideo =
document.getElementById(
    "loadingVideo"
);


// =========================
// VIDEO AL LOGIN
// =========================

form.addEventListener(
    "submit",
    () => {

        loadingScreen.style.display =
        "flex";

        loadingVideo.currentTime = 0;

        loadingVideo.play();

    }
);


// =========================
// LINK REGISTER
// =========================

const registerLink =
document.getElementById(
    "registerLink"
);


// =========================
// VIDEO AL IR A REGISTER
// =========================

registerLink.addEventListener(
    "click",
    function(e){

        e.preventDefault();

        loadingScreen.style.display =
        "flex";

        loadingVideo.currentTime = 0;

        loadingVideo.play();

        // CUANDO TERMINA EL VIDEO

        loadingVideo.onended = () => {

            window.location.href =
            "/register";

        };

        // RESPALDO SI FALLA EL VIDEO

        setTimeout(() => {

            if(
                window.location.pathname !==
                "/register"
            ){

                window.location.href =
                "/register";

            }

        }, 5000);

    }
);