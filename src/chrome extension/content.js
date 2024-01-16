if (!window.urlChecked) {
    chrome.runtime.sendMessage({
        action: "checkUrl",
        url: window.location.href
    });
    window.urlChecked = true;
}
