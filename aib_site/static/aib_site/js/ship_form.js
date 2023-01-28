/** This function takes the id and the ship's name from the item you selected and sets its value to a form that is attached to a modal. Your choice will be saved if you so choose or cancled otherwise.*/
function populateForm(shipName,shipDisplayName){

    document.getElementById("formInput").value = shipName;
    document.getElementById("formText").innerText = `Your choice of ${shipDisplayName} will be submitted now.`;
    
}