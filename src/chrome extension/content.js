const serverUrl = 'http://127.0.0.1:5000';

// // Example: Trigger the Python script when the extension button is clicked
// chrome.browserAction.onClicked.addListener(() => {
//     fetch(`${serverUrl}/run-python-script`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded',
//             // Add any additional headers if needed
//         },
//         // Replace data with the form data you want to send to the server
//         body: 'key1=value1&key2=value2', // Adjust based on your form data
//     })
//     .then(response => response.text())
//     .then(result => console.log(result))
//     .catch(error => console.error(error));
// });

function submitForm() {
    const formData = new FormData(document.getElementById('myForm'));

    fetch(`${serverUrl}/run-python-script`, {
        method: 'POST',
        body: formData,
    })
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.error(error));
}

