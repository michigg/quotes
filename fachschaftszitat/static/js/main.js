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
    var items = document.querySelectorAll(itemSelector);
    items.forEach(function (item) {
        item.style.display = unHideStyle;
    });

    items.forEach(function (item) {
        var quote = item.getElementsByClassName('quote-quote')[0].innerHTML;
        var originator = item.getElementsByClassName('quote-author')[0].innerHTML;

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

function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function cloneMore(selector, prefix) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find('input, select').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    var conditionRow = $('.form-row:not(:last)');
    conditionRow.find('.btn.add-form-row')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row').addClass('remove-form-row')
    .html('<span aria-hidden="true">-</span>');
    return false;
}
function deleteForm(prefix, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row').remove();
        var forms = $('.form-row');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}
$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
    cloneMore('.form-row:last', 'form');
    return false;
});
$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm('form', $(this));
    return false;
});
