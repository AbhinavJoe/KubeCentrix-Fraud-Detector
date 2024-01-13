chrome.runtime.sendMessage({
    action: "check_website",
    url: window.location.href
}, function (response) {
    if (response && response.data && response.data.is_fraudulent) {
        alert("Warning: This website may be fraudulent!");
    }
});
