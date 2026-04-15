function validateForm() {
    let name = document.forms["regForm"]["name"].value;
    let email = document.forms["regForm"]["email"].value;
    let password = document.forms["regForm"]["password"].value;
    let contact = document.forms["regForm"]["contact"].value;
    
    if ( name == "") {
        alert("Name must be filled out");
        return false;
    }

    if (email == "" || !email.includes("@")) {
        alert("Enter valid email");
        return false;
    }

    if (password.length < 6){
        alert("Password must be at least 6 characters");
        return false;
    }

    if (isNaN(contact) || contact.length != 10) {
        alert("Enter valid 10-digit contact number");
        return false;
    }

    return true;
}