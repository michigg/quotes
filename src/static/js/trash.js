function ready(fn) {
    if (document.attachEvent ? document.readyState === "complete" : document.readyState !== "loading") {
        fn();
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

ready(function () {
    initTrash();
});

function initTrash() {
    const trashs = document.getElementsByClassName("trash");
    for (const trash in trashs) {
        trash.addE
    }
}

function confirm_delete() {
    return confirm("Möchtest du das Zitat wirklich löschen?");
}

function resetQuotesAndDisplaySuccess() {
    updateQuotes();
    displaySuccessModal();
}


function deleteQuote(url) {
    const is_confirmed = confirm_delete();
    if (is_confirmed) {
        console.log(url);
        $.ajax({
            url: url,
            type: 'delete',
            dataType: 'json',
            data: {},
            success: resetQuotesAndDisplaySuccess,
            error: displayErrorModal,
        })
    }

}