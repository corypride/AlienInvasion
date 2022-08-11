

window.onload = function () {
    // write the code that changes a picture frame to match any choice in the ship_selector option
   

    let shipSelector = document.getElementById("ship_selector");
    // These two lines of code are to display/set the img window and related info after the user selects a ship


   
    let divIdNum = shipSelector.value;
    showShipInfo(divIdNum);
  
   shipSelector.addEventListener("change" ,function(){
    
    let divIdNum = shipSelector.value;
    showShipInfo(divIdNum);
   });


}


function showShipInfo(divIdNum) {
    //    todo: use the querySelector to find all elements in the 'infoDivs' class and set each of their style.visibility ="hidden" first
    
    let theDivIdstr = "div-"+divIdNum;
    let theDiv = document.getElementById(theDivIdstr);
    console.log(theDiv)
    theDiv.style.visibility="visible";


}