// function loadContent(endpoint) {
//     fetch(`http://localhost:5000/${endpoint}`)
//         .then(response => response.text())
//         .then(html => {
//             document.getElementById('content').innerHTML = html;
//         })
//         .catch(error => console.error('Error:', error));
// }

// document.addEventListener('DOMContentLoaded', () => {
//     loadContent('');

//     // Event listeners for buttons
//     document.getElementById('loadVerification').addEventListener('click', () => {
//         console.log("Verification button clicked");
//         loadContent('verification');
//     });

//     document.getElementById('loadFeedback').addEventListener('click', () => {
//         console.log("Feedback button clicked");
//         loadContent('feedback');
//     });
// });
