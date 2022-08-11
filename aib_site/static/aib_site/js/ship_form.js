// prevValue is a variable that will be used to keep track of the id number of the div of the ship that was previously made visible
let prevValue = 0;

window.onload = function () {
    // write the code that changes a picture frame to match any choice in the ship_selector option

    let shipSelector = document.getElementById("ship_selector");

    //this function is passed the id value of the ship that the user selects in order to make visible the ship image and its related items
    showShipInfo(shipSelector.value);

    shipSelector.addEventListener("change", function () {
        showShipInfo(shipSelector.value);
    });


}


function showShipInfo(divIdNum) {
    

    if (prevValue > 0) {
        document.getElementById("div-" + prevValue).style.visibility = "hidden";
    }
    
    prevValue = divIdNum;
    let theDivIdstr = "div-" + divIdNum;
    let theDiv = document.getElementById(theDivIdstr);
    console.log(theDiv)
    theDiv.style.visibility = "visible";


}