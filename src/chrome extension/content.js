// Replace with your server URL
const serverUrl = 'http://localhost:5000';

// Example: Trigger the Python script when the extension button is clicked
chrome.browserAction.onClicked.addListener(() => {
    fetch(`${serverUrl}/run-python-script`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            // Add any additional headers if needed
        },
        // Replace data with the form data you want to send to the server
        body: 'key1=value1&key2=value2', // Adjust based on your form data
    })
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.error(error));
});

