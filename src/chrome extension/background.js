chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if (changeInfo.status === 'complete' && tab.active) {
        fetch('http://localhost:5000/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                url: tab.url, word_list: [
                    "suspicious",
                    "phishing",
                    "free",
                    "limited time",
                    "money",
                    "earn",
                    "win",
                    "invest",
                    "guaranteed",
                    "miracle",
                    "love",
                    "happy",
                    "success",
                    "dream",
                    "click",
                    "buy",
                    "claim",
                    "order",
                    "banking",
                    "credit",
                    "loan",
                    "investment",
                    "cure",
                    "miracle",
                    "free",
                    "download",
                    "update",
                    "security",
                    "crack",
                    "discount",
                    "sale",
                    "deal",
                    "coupon",
                    "limited"
                ]
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.isFraudulent) {
                    chrome.tabs.sendMessage(tabId, { type: "FRAUD_WARNING" });
                }
            })
            .catch(error => console.error('Error:', error));
    }
});

// Content Script Messaging Listener
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => { // Have to ask GPT 4 why this sender, sendResponse is not getting used in the script
    if (message.type === "FRAUD_WARNING") {
        chrome.notifications.create({
            type: "basic",
            iconUrl: "warning_icon.png",
            title: "Security Alert",
            message: "Warning: This website may be fraudulent."
        });
    }
});


// chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
//     if (changeInfo.status === 'complete' && tab.active) {
//         // Existing code to check for fraudulent website...
//         fetch('http://localhost:5000/scan', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ url: tab.url, word_list: ["suspicious", "phishing"] })
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.isFraudulent) {
//                 // Redirect to the custom HTML page
//                 chrome.tabs.update(tabId, { url: chrome.runtime.getURL("fraud-warning.html") });
//             }
//         })
//         .catch(error => console.error('Error:', error));
//     }
// });
