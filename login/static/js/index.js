
function myFunction(button) {
    if (button == 'register') {
        document.getElementById("login").className = "register-form";
        document.getElementById(button).className = "login-form";
    }
    else if (button == 'login') {
        document.getElementById("register").className = "register-form";
        document.getElementById(button).className = "login-form";
    }
}