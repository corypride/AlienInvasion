/** This function takes the id and the ship's name from the item you selected and sets its value to a form that is attached to a modal. Your choice will be saved if you so choose or cancled otherwise.*/
function populateForm(shipId,shipName){
   
    let capitalShipName = shipName[0].toUpperCase() + shipName.substring(1,shipName.length);
    document.getElementById("formInput").value = shipId;
    document.getElementById("formText").innerText = `Your choice of ${capitalShipName} will be submitted now.`;
    
}