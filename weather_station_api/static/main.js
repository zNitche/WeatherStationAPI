function sendGet(targetURL) {
    let data = fetch(targetURL).then((response)=>response.json()).then((responseJson)=>{return responseJson});

    return data;
}


function sendPost(targetURL, jsonPayload, actionHandler) {
    fetch(targetURL, {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: jsonPayload
    }).then((response)=>response.json())
    .then((responseJson)=>{actionHandler(responseJson)});
}


function displayDate(dateContainerId) {
    const currentDate = new Date();
	const formattedCurrentDate = currentDate.getDate() + "-" + (currentDate.getMonth() + 1) + "-" + currentDate.getFullYear()

	document.getElementById(dateContainerId).innerHTML = formattedCurrentDate;
}
