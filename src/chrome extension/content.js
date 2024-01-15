chrome.runtime.sendMessage({
    action: "checkUrl",
    url: window.location.href
});
