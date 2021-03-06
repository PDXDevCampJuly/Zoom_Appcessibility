/**
 * Created by summerlynbryant on 10/5/15.
 */


var form = document.getElementById('signup');

/// validating certain things get entered into the form
function formValidate(e) {
    e.preventDefault();
    var username = e.target.querySelector("[name=username]");
    if (username.value < 1) {
        alert("You're close, but give me a little something.");
        return false;
    }
    var password = e.target.querySelector("[name=password]");
    if (password.value < 6) {
        alert(" Please use between 6-12 characters");
        return false;
    }
    // Regular expression was used for an exact format for email.
    var email = e.target.querySelector("[name=email]");
    var regex = /[^@]+@[^@]+.[^@]/;
    var valid = regex.test(email.value);
    if (!valid) {
        alert("Entered an invalid email, you have. Enter a valid email, you must");
        return false;
    }
    //this stores the name value so that it can be passed into the gallery
    sessionStorage.setItem("name", username.value);
    // this directs user to the gallery page after all validation has
    // happened for correct information entered
    document.location.href = "zoom/homepage_properties";
}
//this is an event Listener for the submit button click
form.addEventListener("submit", formValidate, false);

