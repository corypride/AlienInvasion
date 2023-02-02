/** This function takes the name from the item you selected and sets its value to a form that is attached to a modal. Your choice will be saved if you so choose or cancled otherwise.*/
function populateForm(invaderName,invaderDisplayName){

    document.getElementById("formInput").value = invaderName;
    document.getElementById("formText").innerText = `Your choice of ${invaderDisplayName} will be submitted now.`;
    
}