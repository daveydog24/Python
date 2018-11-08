// Set a Class User with initial values all undefined
class User{
    constructor() {
        first_name = undefined;
        last_name = undefined;
        email = undefined
    }
}

// once the form is submitted prevent action, store information passed through it, define our User class, manipulate and send an alert
function Submit(event) {
    event.preventDefault();

    let first_name = document.getElementById('first_name').value;
    let last_name = document.getElementById('last_name').value;
    let email = document.getElementById('email').value;
    User.first_name = first_name;
    User.last_name = last_name;
    User.email = email;

    alert(`Hello ${User.first_name} ${User.last_name} welcome to my website. We will send a confirmation to your email at: ${User.email}`)
    document.getElementById("myForm").reset();
}

// once the button is clicked manipulate the DOM with stored user information
function sendAlert(){
    document.getElementById('display').innerHTML = (
        `Hello ${User.first_name} ${User.last_name} you are now stored in our database.`
    );
}
