
function myFunction(button) {
    if (button == 'register') {
        document.getElementById("login").className = "register-form";
        document.getElementById(button).className = "login-form";
        //window.location = "/register"
    }
    else if (button == 'login') {
        document.getElementById("register").className = "register-form";
        document.getElementById(button).className = "login-form";
        //window.location = "/login"
    }
}

$('#form').submit(function(e){
    $.post('/url/', $(this).serialize(), function(data){
       $('.message').html(data.message);
       // of course you can do something more fancy with your respone
    });
    e.preventDefault();
});