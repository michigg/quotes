/**
 * setup JQuery's AJAX methods to setup CSRF token in the request before sending it off.
 * http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
 */
// CONFIG
// const GIFS_ENDPOINT = '/gifs';
const GIFS_FORMULAR = $("#gif-form");

// let source = document.getElementById("entry-template").innerHTML;
// let template = Handlebars.compile(source);

/* jshint esversion: 6 */

/**
 * Cookie setting for django
 *
 * @param name  cookie name
 * @returns {*}
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

GIFS_FORMULAR.submit(function (event) {
    event.preventDefault();
    var url = GIFS_FORMULAR.attr('action');
    $.ajax({
        url: url,
        type: 'post',
        dataType: 'json',
        data: GIFS_FORMULAR.serialize(),
        success: gifSuccessProcess,
        error: displayErrorModal,
    })
});

function clearGIFFormular() {
    GIFS_FORMULAR[0].reset();
}

function gifSuccessProcess(data) {
    // TODO update gifs
    // updateQuotes();
    displaySuccessModal(data);
    clearGIFFormular();
}
