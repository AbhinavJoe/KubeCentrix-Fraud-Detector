chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
    if (changeInfo.url) {
        await checkWebsiteAuthenticity(tabId, changeInfo.url);
    }

    if (changeInfo.status === 'complete' && tab.active) {
        await scanWebsiteContent(tabId, tab.url);
    }
});

async function checkWebsiteAuthenticity(tabId, url) {
    try {
        // Checking SSL
        const sslResponse = await fetch('http://localhost:5000/check_ssl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url }),
        });
        const sslData = await sslResponse.json();

        // Checking Domain Authenticity
        const domainResponse = await fetch('http://localhost:5000/check_domain_authenticity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ domain_name: new URL(url).hostname }),
        });
        const domainData = await domainResponse.json();

        const isFraudulent = isWebsiteFraudulent(sslData, domainData);
        if (isFraudulent) {
            blockSite(tabId, "This website is potentially fraudulent.");
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function blockSite(tabId, message) {
    // chrome.tabs.update(tabId, { url: "http://localhost:5000/blocked" }); // Redirect to a blocked view
    chrome.tabs.update(tabId, { url: chrome.runtime.getURL("http://localhost:5000/blocked") });
    // chrome.notifications.create({
    //     type: "basic",
    //     iconUrl: "icon.png",
    //     title: "Website Blocked",
    //     message: message
    // });
}

function isWebsiteFraudulent(sslData, domainData) {
    // Check SSL status
    if (sslData.ssl === false) {
        return true;  // Consider non-SSL sites as potentially fraudulent
    }

    // Check domain registration date or other domain-related flags
    const recentRegistrationThreshold = 30;
    if (domainData.days_registered < recentRegistrationThreshold) {
        return true;
    }

    // Add more conditions as needed based on the response structure from your Flask app

    return false; // If none of the conditions are met, the site is not considered fraudulent
}

async function loadWordList() {
    const response = await fetch(chrome.runtime.getURL('word_list.json'));
    const data = await response.json();
    return data.words;
}

async function scanWebsiteContent(tabId, url) {
    try {
        const wordList = await loadWordList();  // Load the word list
        const response = await fetch('http://localhost:5000/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                url: url,
                word_list: wordList
            })
        });
        const data = await response.json();

        if (data.isFraudulent) {
            chrome.tabs.sendMessage(tabId, { type: "FRAUD_WARNING" });
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

