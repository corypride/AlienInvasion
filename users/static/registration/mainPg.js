window.onload = function(){

    /*Since the bootstrap4 library does not work on the computer that this app was originally built on I added the bootstrap 4.3 folder into the projects directory and linked the pages to those files. Then because the way that DJANGO uses CSRF to validate forms I could not create a form manually and still be able to validate and receive the POST reaqest, so I used the Django forms framework to utilize that functionality then, used the DOM to add the bootstrap class to these elements. */

    // let uInput = document.getElementById("id_username");
    let test = document.getElementById("theform")
    let a = test.querySelectorAll("input")
    // let pInput = document.getElementById("id_password");

    console.log(a)

    // uInput.className = "form-control"
    // pInput.className = "form-control";
    





}