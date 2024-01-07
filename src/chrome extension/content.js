const apiUrl = 'http://localhost:5000/';
const data = { key1: 'value1', key2: 'value2' };

fetch(apiUrl, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
    .then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
