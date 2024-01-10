// function fetchDataFromServer(endpoint) {
//     return fetch(`http://localhost:5000/${endpoint}`)
//         .then(response => response.json()) // Assuming the server response is JSON
//         .catch(error => console.error('Error fetching data:', error));
// }

// // Listening for messages from popup or content scripts
// chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
//     if (request.action === "fetchData") {
//         // Fetch data based on the request and send response back
//         fetchDataFromServer(request.endpoint).then(data => {
//             sendResponse({ status: "success", data: data });
//         }).catch(error => {
//             sendResponse({ status: "error", error: error });
//         });
//         return true; // Indicates that sendResponse will be called asynchronously
//     }
// });
