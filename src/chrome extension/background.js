chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "checkUrl") {
        fetch('http://localhost:5000/ml_check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: request.url })
        })
            .then(response => response.json())
            .then(data => {
                if (data.result === "Suspicious" && !sender.tab.url.includes("localhost:5000/blocked")) {
                    chrome.tabs.update(sender.tab.id, { url: "http://localhost:5000/blocked" });
                } else {
                    sendResponse({ result: "Legitimate" });
                }
            })
            .catch(error => console.error('Error:', error));
    }
    return true;
});
