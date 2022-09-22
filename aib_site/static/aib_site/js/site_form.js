/** This function takes the id and the sites's name from the item you selected and sets its value to a form that is attached to a modal. Your choice will be saved if you so choose or cancled otherwise.*/
function populateForm(siteName,siteDisplayName){

    document.getElementById("formInput").value = siteName;
    document.getElementById("formText").innerText = `Your choice of ${siteDisplayName} will be submitted now.`;
    
}