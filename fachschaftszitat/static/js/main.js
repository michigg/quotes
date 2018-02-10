/* jshint esversion: 6 */
function ready(fn) {
    if (document.attachEvent ? document.readyState === "complete" : document.readyState !== "loading") {
        fn();
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}


ready(function () {
    var searchfield = document.querySelector("#search");
    searchfield.focus();

    searchFilter(searchfield, ".quotes-quotes", "block");

    var reset = document.querySelector("#reset");

    searchfield.addEventListener('input', function (evt) {
        searchFilter(this, '.quote', 'flex');
    });

    reset.addEventListener("click", resetSearch, false);
});

function searchFilter(searchfield, itemSelector, unHideStyle) {
    console.log(searchfield, itemSelector, unHideStyle);
    var items = document.querySelectorAll(itemSelector);
    console.log(items);
    items.forEach(function (item) {
        item.style.display = unHideStyle;
    });

    items.forEach(function (item) {
        var quote = item.getElementsByClassName('quote-quote')[0].innerHTML;
        var originator = item.getElementsByClassName('quote-author')[0].innerHTML;
        console.log(quote, originator);

        if (!quote.toLowerCase().includes(searchfield.value.toLowerCase()) && !originator.toLowerCase().includes(searchfield.value.toLowerCase())) {
            item.style.display = "none";
        }
    });
}


function resetSearch() {
    var searchfield = document.querySelector("#search");
    var buttons = document.querySelectorAll(".quote");
    searchfield.blur();
    searchfield.value = "";

    buttons.forEach(function (item) {
        item.style.display = "block";
    });

    searchfield.focus();
}