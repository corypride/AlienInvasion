window.onload = function(){
    
    let regFrm = document.getElementById("registerFrm");
    regFrm.addEventListener("submit",function(event){
        // if the form is good then submit
        validateForm(document,event)
    });    
}

// checks an makes sure that all the fields are good
function validateForm(document,event){
    let usrNam = document.getElementById("id_username").value;
    let pswrd1 = document.getElementById("id_password1").value;
    let pswrd2 = document.getElementById("id_password2").value;
    let warnings = document.getElementById("warnings");
   console.log("here "+ pswrd1.localeCompare(pswrd2))
    if (pswrd1.includes(usrNam)){
        event.preventDefault()
        warnings.innerHTML = "Password cannot be to similar or commonly used.";
        
    } else if (pswrd1.length < 8){
        event.preventDefault()
        warnings.innerHTML = "Password must contain at least 8 chars.";
        
    }else if(!isNaN(pswrd1)){
        event.preventDefault();
        warnings.innerHTML ="Password cannot be all numbers.";

    }else if(pswrd1.localeCompare(pswrd2) != 0){
        event.preventDefault();
        warnings.innerHTML ="Password and repeat password must match.";

    }
}