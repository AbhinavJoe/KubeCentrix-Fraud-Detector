// chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
//     if (changeInfo.status === 'complete' && tab.active) {
//         try {
//             const response = await fetch('http://localhost:5000/check_website', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({
//                     url: tab.url,
//                     word_list: await loadWordList()  // Load your word list here
//                 })
//             });

//             const data = await response.json();
//             if (
//                 isWebsiteFraudulent(data)) {
//                 // Send a message to the content script
//                 chrome.tabs.sendMessage(tabId, { type: "FRAUD_WARNING", data: data });
//             }
//         } catch (error) {
//             console.error('Error:', error);
//         }
//     }
// });

// async function loadWordList() {
//     const response = await fetch(chrome.runtime.getURL('../../data/word_list.json'));
//     const data = await response.json();
//     return data.words;
// }

// function isWebsiteFraudulent(data, tabId) {
//     if (!data.ssl_verification || data.suspicious_words) {
//         // Redirect to the custom blocked page
//         chrome.tabs.update(tabId, { url: "http://localhost:5000/blocked" });
//         return true;
//     }
//     return false;
// }

chrome.runtime.onInstalled.addListener(() => {
    // Initialize or perform tasks when the extension is installed/updated
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "check_website") {
        fetch('http://localhost:5000/check_website', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: request.url })
        })
            .then(response => response.json())
            .then(data => {
                sendResponse({ data: data });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    return true;
});
