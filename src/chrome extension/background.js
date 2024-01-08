const serverUrl = 'http://localhost:5000';
const socket = io.connect(serverUrl);

socket.on('update', (data) => {
    console.log('Received update:', data);
    // Process the update as needed
});