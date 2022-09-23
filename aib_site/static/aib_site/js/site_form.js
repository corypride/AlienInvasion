/** This function takes the id and uses it to grab the screen size as well as the sites's name from the item you selected and sets its value to a form that is attached to a modal. Your choice will be saved if you so choose or cancled otherwise.*/
function populateForm(siteName,siteDisplayName,siteId){

    let temp = "screenSize"+siteId;
    let arr = document.getElementById(temp).value.split("X");
    let width = arr[0].trim();
    let height = arr[1].trim();

    document.getElementById("siteInput").value = siteName;
    document.getElementById("widthInput").value = width;
    document.getElementById("heightInput").value = height;
    
    
    document.getElementById("formText").innerText = `Your choice of ${siteDisplayName}, with the screen size set at ${width} X ${height} will be submitted now.`;
    
}


